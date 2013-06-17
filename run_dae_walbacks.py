
import argparse
import model

def main():
    parser = argparse.ArgumentParser()
    # Add options here
    args = parser.parse_args()
    
    args.K          =   1
    args.N          =   1
    args.n_epoch    =   1000
    args.batch_size =   100

    #args.hidden_add_noise_sigma =   1e-10
    
    args.hidden_add_noise_sigma =   0
    args.input_salt_and_pepper  =   0.4

    args.learning_rate  =   10
    args.momentum       =   0.
    args.annealing      =   1

    args.hidden_size    =   2000

    args.input_sampling =   True
    args.noiseless_h1   =   True

    args.vis_init       =   False
    
    #args.act            =   'rectifier'
    args.act            =   'sigmoid'

    args.dataset        = 'MNIST_binary'
    args.data_path      =   '.'

    args.test           =   True

    model.experiment(args, None)
    
if __name__ == '__main__':
    main()