# Gym Retro

[Gym Retro](https://blog.openai.com/gym-retro/) is a platform for [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) research on games. It turns out that old games are a perfect fit for benchmarking and improving RL agents in a simulated environment. After two years after the beta release of [Gym](https://blog.openai.com/openai-gym-beta/), OpenAI released an extension of this amazing software by adding more game environments. The goal of the new platform is to study the ability of the agents to *generalize* between games with similar concepts but different appearances.

![retro gif](https://github.com/floydhub/gym-retro-template/raw/master/images/retro.gif)

### Try it now

[![Run on FloydHub](https://s3-us-west-2.amazonaws.com/floydhub-assets/button/button.svg)](https://floydhub.com/run?template=https://github.com/floydhub/gym-retro-template)

Click this button to open a Workspace on FloydHub that will setup Gym-Retro.

## Gym Retro Contest - Sonic The Hedgehog™

[In this contest](https://blog.openai.com/retro-contest/), participants try to create the best agent for playing custom levels of the Sonic games — without having access to those levels during development. You can find more detail in this [page](https://contest.openai.com/details).

As mentioned in the contest's description this is a Transfer Learning task, which means that you are free to train your agent however you'd like, however, the OpenAI Team recommend using Sonic 1, 2, and 3 & Knuckles, which are available on Steam here:

- [Sonic The Hedgehog](http://store.steampowered.com/app/71113/Sonic_The_Hedgehog/)
- [Sonic The Hedgehog 2](http://store.steampowered.com/app/71163/Sonic_The_Hedgehog_2/)
- [Sonic 3 & Knuckles](http://store.steampowered.com/app/71162/Sonic_3___Knuckles/)

In this notebook, we will show you how to use set up Gym-Retro on FloydHub.

We will:

- Install Gym-Retro
- Import and load the ROMs of the games
- Use random-policy for a couple of steps
- Visualize the agents