# Execute from MetaSkillLearning/Experiments directory: 

# Debug
python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="debug"

# Run
python cluster_run.py --partition=learnfair --name=RL001 --cmd='python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL002 --cmd='python Run_Robosuite_PPO.py --env="SawyerStack" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL003 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlace" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL004 --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssembly" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL005 --cmd='python Run_Robosuite_PPO.py --env="BaxterLift" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL006 --cmd='python Run_Robosuite_PPO.py --env="BaxterPegInHole" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL007 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceBread" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL008 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceCan" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL009 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceCereal" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL010 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceMilk" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL011 --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssemblyRound" --run_name="2"'

python cluster_run.py --partition=learnfair --name=RL012 --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssemblySquare" --run_name="2"'

# Eval

# Debug
python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="2" --no-train

python cluster_run.py --partition=learnfair --name=RL001 --cmd='python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL002 --cmd='python Run_Robosuite_PPO.py --env="SawyerStack" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL003 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlace" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL004 --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssembly" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL005 --cmd='python Run_Robosuite_PPO.py --env="BaxterLift" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL006 --cmd='python Run_Robosuite_PPO.py --env="BaxterPegInHole" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL007 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceBread" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL008 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceCan" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL009 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceCereal" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL010 --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceMilk" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL011 --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssemblyRound" --run_name="2" --no-train'

python cluster_run.py --partition=learnfair --name=RL012 --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssemblySquare" --run_name="2" --no-train'

# Viz

# Eval

# Debug
python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="2" --no-train --evaluate=0

python cluster_run.py --partition=learnfair --name=RL001_render --cmd='python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL002_render --cmd='python Run_Robosuite_PPO.py --env="SawyerStack" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL003_render --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlace" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL004_render --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssembly" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL005_render --cmd='python Run_Robosuite_PPO.py --env="BaxterLift" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL006_render --cmd='python Run_Robosuite_PPO.py --env="BaxterPegInHole" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL007_render --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceBread" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL008_render --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceCan" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL009_render --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceCereal" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL010_render --cmd='python Run_Robosuite_PPO.py --env="SawyerPickPlaceMilk" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL011_render --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssemblyRound" --run_name="2" --no-train --evaluate=0'

python cluster_run.py --partition=learnfair --name=RL012_render --cmd='python Run_Robosuite_PPO.py --env="SawyerNutAssemblySquare" --run_name="2" --no-train --evaluate=0'


# Running Hierarchical PPO to debug. 
python Run_Robosuite_PPO.py --env="SawyerLift" --run_name="hierarchy_debug" --hierarchical=1 

# Running Hierarchical PPO on all environments. 
python cluster_run.py --partition=learnfair --name=HRL001 --cmd='python Run_Robosuite_PPO.py --run_name="HRL001" --hierarchical=1 --env="SawyerLift"'

python cluster_run.py --partition=learnfair --name=HRL002 --cmd='python Run_Robosuite_PPO.py --run_name="HRL002" --hierarchical=1 --env="SawyerStack"'

python cluster_run.py --partition=learnfair --name=HRL003 --cmd='python Run_Robosuite_PPO.py --run_name="HRL003" --hierarchical=1 --env="SawyerPickPlace"'

python cluster_run.py --partition=learnfair --name=HRL004 --cmd='python Run_Robosuite_PPO.py --run_name="HRL004" --hierarchical=1 --env="SawyerNutAssembly"'

python cluster_run.py --partition=learnfair --name=HRL005 --cmd='python Run_Robosuite_PPO.py --run_name="HRL005" --hierarchical=1 --env="BaxterLift"'

python cluster_run.py --partition=learnfair --name=HRL006 --cmd='python Run_Robosuite_PPO.py --run_name="HRL006" --hierarchical=1 --env="BaxterPegInHole"'

python cluster_run.py --partition=learnfair --name=HRL007 --cmd='python Run_Robosuite_PPO.py --run_name="HRL007" --hierarchical=1 --env="SawyerPickPlaceBread"'

python cluster_run.py --partition=learnfair --name=HRL008 --cmd='python Run_Robosuite_PPO.py --run_name="HRL008" --hierarchical=1 --env="SawyerPickPlaceCan"'

python cluster_run.py --partition=learnfair --name=HRL009 --cmd='python Run_Robosuite_PPO.py --run_name="HRL009" --hierarchical=1 --env="SawyerPickPlaceCereal"'

python cluster_run.py --partition=learnfair --name=HRL010 --cmd='python Run_Robosuite_PPO.py --run_name="HRL010" --hierarchical=1 --env="SawyerPickPlaceMilk"'

python cluster_run.py --partition=learnfair --name=HRL011 --cmd='python Run_Robosuite_PPO.py --run_name="HRL012" --hierarchical=1 --env="SawyerNutAssemblyRound"'

python cluster_run.py --partition=learnfair --name=HRL012 --cmd='python Run_Robosuite_PPO.py --run_name="HRL013" --hierarchical=1 --env="SawyerNutAssemblySquare"'

#####################################################


# Running Hierarchical PPO on all environments. 
# trial 
python Run_Robosuite_PPO.py --run_name="trial" --hierarchical=1 --env="SawyerLift"

python Run_Robosuite_PPO.py --run_name="HRL001" --hierarchical=1 --env="SawyerLift"

python Run_Robosuite_PPO.py --run_name="HRL002" --hierarchical=1 --env="SawyerStack"

python Run_Robosuite_PPO.py --run_name="HRL003" --hierarchical=1 --env="SawyerPickPlace"

# 
# Run without hierarchy for comparison
python Run_Robosuite_PPO.py --run_name="RL001" --hierarchical=0 --env="SawyerLift"

python Run_Robosuite_PPO.py --run_name="RL002" --hierarchical=0 --env="SawyerStack"

python Run_Robosuite_PPO.py --run_name="RL003" --hierarchical=0 --env="SawyerPickPlace"

python Run_Robosuite_PPO.py --run_name="HRL004" --hierarchical=1 --env="SawyerNutAssembly"

python Run_Robosuite_PPO.py --run_name="HRL005" --hierarchical=1 --env="BaxterLift"

python Run_Robosuite_PPO.py --run_name="HRL006" --hierarchical=1 --env="BaxterPegInHole"

python Run_Robosuite_PPO.py --run_name="HRL007" --hierarchical=1 --env="SawyerPickPlaceBread"

python Run_Robosuite_PPO.py --run_name="HRL008" --hierarchical=1 --env="SawyerPickPlaceCan"

python Run_Robosuite_PPO.py --run_name="HRL009" --hierarchical=1 --env="SawyerPickPlaceCereal"

python Run_Robosuite_PPO.py --run_name="HRL010" --hierarchical=1 --env="SawyerPickPlaceMilk"

python Run_Robosuite_PPO.py --run_name="HRL012" --hierarchical=1 --env="SawyerNutAssemblyRound"

python Run_Robosuite_PPO.py --run_name="HRL013" --hierarchical=1 --env="SawyerNutAssemblySquare"

# Trial
python Run_Robosuite_PPO.py --run_name="trailzz" --hierarchical=1 --env="SawyerNutAssembly" --data=Roboturk
# 
python Run_Robosuite_PPO.py --run_name="trailzz" --hierarchical=0 --env="SawyerNutAssembly" --data=Roboturk
#
# Trial with model
# python Run_Robosuite_PPO.py --run_name="trail_with_model" --hierarchical=1 --env="SawyerNutAssembly" --data=Roboturk --lowlevel_policy_model="~/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340"

python Run_Robosuite_PPO.py --run_name="trail_with_model" --hierarchical=1 --env="SawyerNutAssembly" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_001/saved_models/Model_epoch105"

# Actually run on easy tasks
python Run_Robosuite_PPO.py --run_name="HRL_100" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_001/saved_models/Model_epoch105" --target_kl=0.03

python Run_Robosuite_PPO.py --run_name="HRL_101" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_001/saved_models/Model_epoch105" --target_kl=0.04

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_102" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_001/saved_models/Model_epoch105" --target_kl=0.05

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_101" --hierarchical=1 --env="SawyerStack" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_001/saved_models/Model_epoch105"

# python Run_Robosuite_PPO.py --run_name="HRL_102" --hierarchical=1 --env="SawyerLift" --data=Roboturk

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_103" --hierarchical=1 --env="SawyerStack" --data=Roboturk

# Contrasting run
CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="RL_101" --hierarchical=0 --env="SawyerLift"

# 
python Run_Robosuite_PPO.py --run_name="HRL_106" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=2.

python Run_Robosuite_PPO.py --run_name="HRL_107" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=5.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_108" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=10.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_109" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.


#################################################################

# Debug
python Run_Robosuite_PPO.py --run_name="HRL_debug" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

#
# Run with.. hierachy, loading model
python Run_Robosuite_PPO.py --run_name="HRL_201" --hierarchical=1 --env="SawyerLift" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

python Run_Robosuite_PPO.py --run_name="HRL_202" --hierarchical=1 --env="SawyerStack" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_203" --hierarchical=1 --env="SawyerPickPlaceBread" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_204" --hierarchical=1 --env="SawyerPickPlaceCan" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

python Run_Robosuite_PPO.py --run_name="HRL_205" --hierarchical=1 --env="SawyerPickPlaceCereal" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

python Run_Robosuite_PPO.py --run_name="HRL_206" --hierarchical=1 --env="SawyerPickPlaceMilk" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_207" --hierarchical=1 --env="SawyerNutAssemblyRound" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_208" --hierarchical=1 --env="SawyerNutAssemblySquare" --data=Roboturk --lowlevel_policy_model="/home/tshankar/Research/Code/CausalSkillLearning/Experiments/ExpWandbLogs/RTP_051/saved_models/Model_epoch340" --action_scaling=1.

# Run without hierarchy
CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_301" --hierarchical=0 --env="SawyerLift" --data=Roboturk --action_scaling=1.

CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_302" --hierarchical=0 --env="SawyerStack" --data=Roboturk --action_scaling=1.

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_303" --hierarchical=0 --env="SawyerPickPlaceBread" --data=Roboturk --action_scaling=1.

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_304" --hierarchical=0 --env="SawyerPickPlaceCan" --data=Roboturk --action_scaling=1.

# CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_305" --hierarchical=0 --env="SawyerPickPlaceCereal" --data=Roboturk --action_scaling=1.

# CUDA_VISIBLE_DEVICES=0 python Run_Robosuite_PPO.py --run_name="HRL_306" --hierarchical=0 --env="SawyerPickPlaceMilk" --data=Roboturk --action_scaling=1.

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_307" --hierarchical=0 --env="SawyerNutAssemblyRound" --data=Roboturk --action_scaling=1.

# CUDA_VISIBLE_DEVICES=1 python Run_Robosuite_PPO.py --run_name="HRL_308" --hierarchical=0 --env="SawyerNutAssemblySquare" --data=Roboturk --action_scaling=1.


# Run with hierarchy, no loading model
python Run_Robosuite_PPO.py --run_name="HRL_211" --hierarchical=1 --env="SawyerLift" --data=Roboturk --action_scaling=1.

python Run_Robosuite_PPO.py --run_name="HRL_212" --hierarchical=1 --env="SawyerStack" --data=Roboturk --action_scaling=1.
