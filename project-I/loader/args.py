import argparse

def get_args(local=False):
    parser = argparse.ArgumentParser()

    if local:
        # Load and train arguments
        parser.add_argument('--data_dir_train', type=str, default='data/Final_Training/Images',
                           help='data directory containing training image class folders')
        parser.add_argument('--data_dir_test', type=str, default='data/Final_Test',
                           help='data directory containing test images')
        parser.add_argument('--annotations_file', type=str, default='data/Final_Training/Annotations',
                           help='data directory containing class annotations file')
        parser.add_argument('--data_dir_val', type=str, default='data/Final_Validation',
                           help='data directory containing validation images')
        parser.add_argument('--log_dir', type=str, default='logs',
                           help='directory containing logs')
        parser.add_argument('--save_dir', type=str, default='save',
                           help='directory to store checkpointed models')
    else:
        parser.add_argument('--data_dir_train', type=str, default='/content/Final_Training/Images',
                           help='data directory containing training image class folders')
        parser.add_argument('--data_dir_test', type=str, default='data/Final_Test',
                           help='data directory containing test images')
        parser.add_argument('--annotations_file', type=str, default='/content/Final_Training/Annotations',
                           help='data directory containing class annotations file')
        parser.add_argument('--data_dir_val', type=str, default='/content/Final_Validation',
                           help='data directory containing validation images')
        parser.add_argument('--log_dir', type=str, default='logs',
                           help='directory containing logs')
        parser.add_argument('--save_dir', type=str, default='save',
                           help='directory to store checkpointed models')
    
    parser.add_argument('--batch_size', type=int, default=50,
                       help='input batch size for training')
    parser.add_argument('--num_epochs', type=int, default=8,
                       help='number of epochs to train')
    parser.add_argument('--learning_rate', type=float, default=0.0001,
                        help='learning rate (default: 0.0001)')
    parser.add_argument('--seed', type=int, default=1,
                        help='random seed (default: 1)')
    parser.add_argument('--log-interval', type=int, default=100,
                        help='how many batches to wait before logging training status')
    parser.add_argument('--save_every', type=int, default=1000,
                       help='save frequency')
    parser.add_argument('--decay_rate', type=float, default=0.97,
                       help='decay rate for rmsprop')
    parser.add_argument('--gpu_mem', type=float, default=0.666,
                       help='%% of gpu memory to be allocated to this process. Default is 66.6%%')
    args = parser.parse_args(args=[])
    
    return args


'''
    parser.add_argument('--init_from', type=str, default=None,
                       help="""continue training from saved model at this path.
                            'config.pkl'        : configuration;
                            'checkpoint'        : paths to model file(s) (created by tf).
                                                  Note: this file contains absolute paths, be careful when moving files around;
                            'model.ckpt-*'      : file(s) with model definition (created by tf)
                        """)
'''