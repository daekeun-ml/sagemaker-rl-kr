# Amazon SageMaker RL상에서 stable baseline으로 Roboschool 시뮬레이션 훈련

Roboschool은 로봇 시스템에 대한 RL 정책을 훈련시키는 데 일반적으로 사용되는 [오픈 소스](https://github.com/openai/roboschool/tree/master/roboschool) 물리 시뮬레이터입니다. Roboschool은 다양한 로봇 문제에 해당하는 [다양한](https://github.com/openai/roboschool/blob/master/roboschool/__init__.py) gym 환경들을 제공합니다. 그 중 하나는 **HalfCheetah** 입니다. 이것은 다리가 두 개인 로봇으로, 수직 면(vertical plane)으로 제한되어 있어 앞,뒤로만 움직일 수 있습니다.

이 노트북 예제에서는 **HalfCheetah**가 걷는 법을 배우며, [OpenAI Baselines](https://github.com/openai/baselines) 를 기반으로 한 개선된 RL (Reinforcement Learning) 알고리즘의 구현체인 [stable-baselines](https://stable-baselines.readthedocs.io/en/master/) 를 사용합니다.


## Contents

* `rl_roboschool_stable_baselines.ipynb`: *HalfCheetah*가 걷는 법을 배우게 하는 코드를 보여주는 노트북
* `Dockerfile`: Dockerfile은 SageMaker의 RL tensorflow 컨테이너를 기본으로 사용하여 Roboschool, OpenMPI, stable-baselines 및 해당 의존성 패키지들로 컨테이너 빌드
* `src/`
  * `preset-half-cheetah.py`: Stable-Baselines PPI1을 사용한 HalfCheetah 분산 훈련에 대한 사전 설정(preset)
  * `train_stable_baselines.py`: Stable-Baselines 런처 훈련 스크립트
* `resources`: 도커 빌드의 일부로 필요한 파일들
* `examples`: `10 ml.c4.xlarge` 인스턴스와 `num_timesteps = 1e7` 인 `rl_roboschool_stable_baselines.ipynb` 노트북을 사용하여 훈련된 모델에 대한 RL 비디오 출력 결과
