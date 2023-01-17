import streamlit as st
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import to_categorical

# MNISTデータの読み込み
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 入力データの整形
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# ターゲットデータの整形
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# アルゴリズムの選択
st.sidebar.title("Optimization Algorithm")
algorithm = st.sidebar.selectbox("Select optimization algorithm", ["Adam", "SGD", "Adagrad"])

# ニューラルネットワークの構築
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dense(10, activation='softmax'))

# コンパイル
if algorithm == "Adam":
    optimizer = Adam()
elif algorithm == "SGD":
    optimizer = SGD()
else:
    optimizer = Adagrad()

model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# 学習
epochs = st.sidebar.slider("Select number of epochs", 1, 30)
model.fit(X_train, y_train, epochs=epochs, verbose=1)

# 評価
score = model.evaluate(X_test, y_test, verbose=0)
st.write("Test loss:", score[0])
st.write("Test accuracy:", score[1])

