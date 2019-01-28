### sgm

Python port of [seeded graph matching (SGM)](https://arxiv.org/pdf/1209.0367.pdf)

#### Quickstart

```
# make fresh conda env
conda create -n sgm_env python=3.6 pip -y
source activate sgm_env

# install requirements
cat requirements.txt | xargs -I {} pip install {}

# install sgm
pip install -e .
```

#### Example Usage

```
cd examples/synthetic
python main.py
```