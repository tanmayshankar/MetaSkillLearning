import torch, torch.nn as nn, numpy as np, sys
sys.path.append("/private/home/tanmayshankar/Research/Code/spinningup")
from IPython import embed
from spinup.exercises.pytorch.problem_set_1 import exercise1_1
from spinup.exercises.pytorch.problem_set_1 import exercise1_2_auxiliary
from spinup.utils.run_utils import ExperimentGrid

"""

Exercise 1.2: PPO Gaussian Policy

You will implement an MLP diagonal Gaussian policy for PPO by
writing an MLP-builder, and a few other key functions.

Log-likelihoods will be computed using your answer to Exercise 1.1,
so make sure to complete that exercise before beginning this one.

"""

def mlp(sizes, activation, output_activation=nn.Identity):
    """
    Build a multi-layer perceptron in PyTorch.

    Args:
        sizes: Tuple, list, or other iterable giving the number of units
            for each layer of the MLP. 

        activation: Activation function for all layers except last.

        output_activation: Activation function for last layer.

    Returns:
        A PyTorch module that can be called to give the output of the MLP.
        (Use an nn.Sequential module.)

    """
    layers = []
    for j in range(len(sizes)-1):
        act = activation if j < len(sizes)-2 else output_activation
        layers += [nn.Linear(sizes[j], sizes[j+1]), act()]
    return nn.Sequential(*layers)

def gaussian_likelihood(x, mu, log_std):
    pre_sum = -0.5 * (((x-mu)/(torch.exp(log_std)+EPS))**2 + 2*log_std + np.log(2*np.pi))
    return pre_sum.sum(axis=-1)


class MLPGaussianActor(nn.Module):


    def __init__(self, obs_dim, act_dim, hidden_sizes, activation):
        super().__init__()

        self.mu_net = mlp([obs_dim] + list(hidden_sizes) + [act_dim], activation)      
        self.std_net = mlp([obs_dim] + list(hidden_sizes) + [act_dim], activation)
        self.softplus_activation = torch.nn.Softplus()

    def forward(self, obs, act=None):

        # Create mean and var. 
        mean = self.mu_net(obs)
        standard_deviation = self.softplus_activation(self.std_net(obs))

        # Distribution. 
        dist = torch.distributions.MultivariateNormal(mean, torch.diag_embed(standard_deviation))

        log_prob = None
        if act is not None:
            log_prob = dist.log_prob(act)

        return dist, log_prob


if __name__ == '__main__':
    """
    Run this file to verify your solution.
    """

    from spinup import ppo_pytorch as ppo
    from spinup.exercises.common import print_result
    from functools import partial
    import gym
    import os
    import pandas as pd
    import psutil
    import time
    import robosuite
    from robosuite.wrappers import GymWrapper

    base_env = robosuite.make("SawyerLift", has_renderer=False, use_camera_obs=False, reward_shaping=True)

    gym_env = GymWrapper(base_env)

    logdir = "/tmp/experiments/%i"%int(time.time())

    ActorCritic = partial(exercise1_2_auxiliary.ExerciseActorCritic, actor=MLPGaussianActor)

    ppo(env_fn = lambda : gym_env,
        actor_critic=ActorCritic,
        ac_kwargs=dict(hidden_sizes=(64,)),
        steps_per_epoch=4000, epochs=100, logger_kwargs=dict(output_dir=logdir))

    # Get scores from last five epochs to evaluate success.
    data = pd.read_table(os.path.join(logdir,'progress.txt'))
    last_scores = data['AverageEpRet'][-5:]

    print_result(last_scores)

    # ##########################################
    # # Code from Spinning up examples that uses the experiment grid function to create sweep.
    # ##########################################

    # parser = argparse.ArgumentParser()
    # parser.add_argument('--cpu', type=int, default=4)
    # parser.add_argument('--num_runs', type=int, default=3)
    # args = parser.parse_args()

    # eg = ExperimentGrid(name='ppo-pyt-bench')
    # eg.add('env_name', 'CartPole-v0', '', True)
    # eg.add('seed', [10*i for i in range(args.num_runs)])
    # eg.add('epochs', 10)
    # eg.add('steps_per_epoch', 4000)
    # eg.add('ac_kwargs:hidden_sizes', [(32,), (64,64)], 'hid')
    # eg.add('ac_kwargs:activation', [torch.nn.Tanh, torch.nn.ReLU], '')
    # eg.run(ppo_pytorch, num_cpu=args.cpu)