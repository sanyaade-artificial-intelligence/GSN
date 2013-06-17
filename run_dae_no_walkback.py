"""
This script will train a single layer model of Generative Denoising Auto-encoder
WITHOUT walkback training.

Reference:
Generalized Denoising Auto-Encoders as Generative Models
http://arxiv.org/abs/1305.6663

Note:
This script will produce a better model than the one in the paper as it has a higher
log-likelihood score (see Table 1 in the above paper) estimated by the Parzen density
estimator. Training for more than 200 epochs would produce a estimated log-likelihood
around -10 or higher.   
"""
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