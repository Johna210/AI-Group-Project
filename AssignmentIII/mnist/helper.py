import math


def flatten(array):
    flat = []
    for item in array:
        try:
            iter(item)
            flat.extend(flatten(item))
        except:
            flat.append(item)
    return flat


def reshape(array, rows, cols):
    flat_array = flatten(array)


    if rows * cols != len(flat_array):
        raise Exception(f"Can't reshape array to ({rows}, {cols})")

    reshaped = [[0] * cols for _ in range(rows)]    

    for row in range(rows):
        for col in range(cols):
            reshaped[row][col] = flat_array[row * cols + col]

    return reshaped

def compute_gradients(image):
    height = len(image)
    width = len(image[0])
    
    gradient_x = [[0]*width for _ in range(height)]
    gradient_y = [[0]*width for _ in range(height)]
    
    for i in range(1, height-1):
        for j in range(1, width-1):
            gradient_x[i][j] = image[i+1][j] - image[i-1][j]
            gradient_y[i][j] = image[i][j+1] - image[i][j-1]
    
    return gradient_x, gradient_y

# Function to compute the magnitude and orientation of gradients
def compute_magnitude_orientation(gradient_x, gradient_y):
    height = len(gradient_x)
    width = len(gradient_x[0])
    
    magnitude = [[0]*width for _ in range(height)]
    orientation = [[0]*width for _ in range(height)]
    
    for i in range(height):
        for j in range(width):
            magnitude[i][j] = math.sqrt(gradient_x[i][j]**2 + gradient_y[i][j]**2)
            orientation[i][j] = math.degrees(math.atan2(gradient_y[i][j], gradient_x[i][j])) % 180
    
    return magnitude, orientation

# Function to compute the histogram of gradients
def compute_hog(image, cell_size=8, bin_size=9):
    gradient_x, gradient_y = compute_gradients(image)
    magnitude, orientation = compute_magnitude_orientation(gradient_x, gradient_y)
    
    height = len(image)
    width = len(image[0])
    
    num_cells_x = width // cell_size
    num_cells_y = height // cell_size
    
    hist = [[[0]*bin_size for _ in range(num_cells_x)] for _ in range(num_cells_y)]
    
    for i in range(num_cells_y):
        for j in range(num_cells_x):
            for y in range(cell_size):
                for x in range(cell_size):
                    bin_index = int(orientation[i*cell_size + y][j*cell_size + x] / 180 * bin_size)
                    hist[i][j][bin_index] += magnitude[i*cell_size + y][j*cell_size + x]
    
    hog_features = []
    for row in hist:
        for cell in row:
            hog_features.extend(cell)
    
    return hog_features

# Function to perform PCA
def compute_pca(data, num_components):
    # Step 1: Standardize the data
    mean_vector = [sum(col) / len(col) for col in zip(*data)]
    data_centered = [[data[row][col] - mean_vector[col] for col in range(len(data[0]))] for row in range(len(data))]
    
    # Step 2: Compute the covariance matrix
    covariance_matrix = [[sum(data_centered[row][col1] * data_centered[row][col2] for row in range(len(data_centered))) / len(data_centered) for col2 in range(len(data_centered[0]))] for col1 in range(len(data_centered[0]))]
    
    # Step 3: Compute the eigenvectors and eigenvalues
    eigenvectors = [[0]*len(covariance_matrix) for _ in range(len(covariance_matrix))]
    eigenvalues = [0]*len(covariance_matrix)
    
    for i in range(len(covariance_matrix)):
        eigenvalues[i] = covariance_matrix[i][i]
        eigenvectors[i][i] = 1
    
    # Sort the eigenvectors by decreasing eigenvalues
    indices = list(range(len(eigenvalues)))
    indices.sort(key=lambda x: eigenvalues[x], reverse=True)
    
    sorted_eigenvectors = [eigenvectors[i] for i in indices[:num_components]]
    
    # Step 4: Transform the original data
    pca_data = [[sum(data[row][col] * sorted_eigenvectors[col][component] for col in range(len(data[0]))) for component in range(num_components)] for row in range(len(data))]
    
    return pca_data



def sigmoid_scaler(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_vector(X):
    flat = flatten(X)

    for i in range(len(flat)):
        flat[i] = sigmoid_scaler(flat[i])

    return flat


def predict(sample_x, weight):
    # calculate z = sum(w * x + b)
    # here bias (b) is also included in weight
    z = 0
    for x, w in zip(sample_x, weight):
        z += w * x

    # sigmoid(z)
    return sigmoid_scaler(z)


def cross_entropy_loss(predicted_value, actual_value):
    y = actual_value
    y_pred = predicted_value

    if y == 1:
        return -math.log(y_pred + 0.000001)

    else:
        return -math.log(1 - y_pred + 0.000001)


def cost_function(datas, target, weight, bias):
    cost = 0

    for x, y in zip(datas, target):
        y_pred = predict(x, weight, bias)

        cost += cross_entropy_loss(y_pred, y)

    return cost / len(datas)


def gradient_decent(X, label, weight=None, learning_rate=0.1):
    n_features = len(X[0])

    if weight == None:
        weight = [0] * n_features

    loss = 0

    for x, y in zip(X, label):
        y_pred = predict(x, weight)
        loss += cross_entropy_loss(y_pred, y)

        # dw = (y_pred - y) * x
        # weight = weight - learning_rate * dw
        err = y_pred - y
        for i in range(n_features):
            dw_i = err * x[i]
            weight[i] -= learning_rate * dw_i

    return weight, loss / len(X)


def train(x_train, y_train, learning_rate, epoch, verbose=False):
    weight = [0] * len(x_train[0])

    history = []

    for i in range(epoch):
        weight, loss = gradient_decent(x_train, y_train, weight, learning_rate)

        history.append(loss)

        if verbose:
            print(f"Epoch [{i}]\n\t- Cross entropy loss: {loss}")

    return weight, history