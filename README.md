# ef-lab-plugins

Shared plugin library for [EthoPy](https://github.com/ef-lab/ethopy) behavioral experiments.
All lab plugins live in one place — no duplication, one repo to update.

## Structure

```
ef-lab-plugins/
├── behaviors/          # Behavior classes (animal tracking, position, lick detection)
│   ├── openfield.py        # Open field arena with DeepLabCut tracking
│   └── vr_ball.py          # Spherical treadmill / VR ball navigation
├── experiments/        # Experiment state machines
│   ├── match_to_sample.py  # Match-to-sample task (works with Panda3D and PsychoPy stimuli)
│   ├── approach.py         # Approach task for open field
│   └── navigate.py         # Navigation task for VR ball
├── stimuli/            # Stimulus classes
│   ├── panda.py            # Panda3D 3D object stimuli (standard)
│   ├── openfield_panda.py  # Panda3D stimuli with DLC pose-based perspective
│   ├── psycho_grating.py   # PsychoPy grating stimuli
│   ├── psycho_presenter.py # PsychoPy window/flip manager
│   ├── olfactory.py        # Olfactory (odor) stimuli
│   ├── vr_odors.py         # VR odor gradients for ball navigation
│   ├── tones.py            # Auditory tone stimuli
│   └── tones_grating.py    # Combined auditory + visual grating stimuli
├── tasks/              # Ready-to-run task scripts (one per experiment setup)
│   ├── panda_test.py       # Match-to-sample with Panda3D objects
│   ├── openfield_task.py   # Approach task in open field arena
│   ├── psychopy_test.py    # Match-to-sample with PsychoPy gratings
│   ├── ball_test.py        # VR ball navigation with odors
│   ├── tones_test.py       # Auditory discrimination
│   ├── tones_grating_test.py # Audiovisual discrimination
│   └── grating_test.py     # Grating discrimination with Bpod
└── utils/              # Utility scripts
    ├── upload_objects.py   # Upload 3D object files to the stimulus database
    └── export/             # NWB export utilities
        ├── add_dlc_nwb.py      # Export DLC pose data to NWB
        ├── add_video_nwb.py    # Export behavioral video to NWB
        └── add_treadmill_nwb.py # Export treadmill tracking to NWB
```

## Setup

Point `ETHOPY_PLUGIN_PATH` to this repository so EthoPy picks up all plugins:

```bash
export ETHOPY_PLUGIN_PATH=/path/to/ef-lab-plugins
```

Or set it permanently in your EthoPy local config.

## Adding or changing a plugin

Changes to this repository go through a Pull Request (PR) so that someone can review them before they land on `main`. You do not need to know anything about CI or linting — the checks run automatically when you open a PR.

### Step-by-step

1. Create a new branch for your change:
   ```bash
   git checkout -b my-new-plugin
   ```
2. Place your file in the appropriate folder (`behaviors/`, `stimuli/`, `experiments/`, `tasks/`, or `utils/`) and follow the naming and class conventions of existing files.
3. Commit and push your branch:
   ```bash
   git add your_file.py
   git commit -m "add: short description of what this does"
   git push origin my-new-plugin
   ```
4. Open a Pull Request on GitHub. A short checklist will appear — fill it in.
5. Wait for the automated checks to pass (green ✓) and for a reviewer to approve. Once approved the PR can be merged into `main`.

### Automated checks

Every PR automatically runs a syntax and error check ([ruff](https://github.com/astral-sh/ruff)). If something is wrong you will see a red ✗ on the PR — click "Details" to see which file and line has the problem. You do not need to install or run ruff yourself.

### Who reviews?

At least one lab member with write access must approve a PR before it can be merged.
