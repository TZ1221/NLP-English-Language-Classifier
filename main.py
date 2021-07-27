import sys
import pickle
import os

from d_model import DecisionModel



def train(examples, out_file):

    model = DecisionModel(train_file=examples, out_file=out_file)
    model.train()


def predict(h_file, test_file):

    h_file = open(h_file, "rb")
    model = pickle.load(h_file)

    h_file.close()
    model.test(test_file)



def main():

    examples='in/train.dat'
    out_file='out/tree.oj'
    print("Training...")
    train(examples, out_file)
    print("...Training Done.")
    
    
    modelFound = False
    modelDir = "out"


    h_file = open(modelDir + "/" + 'tree.oj', "rb")
    model = pickle.load(h_file)
    h_file.close()
    modelFound = True
    while True:
        print ('due to the small size of trainning data,the accuracy is not that great. Try  words like gaat and going')
        line = input("Enter a word to predict or \"Quit\": ")
        if line == "q" or line=='Quit':
            break
        else:
            model.predict(line)

    print("------Quited--------")



if __name__ == '__main__':

    main()
