# Amazon SageMaker RL을 활용한 예측 오토스케일링

이 예는 강화 학습(RL; Reinforcement Learning) 기술을 사용하여 소프트웨어 시스템의 프로덕션 운영에서 매우 일반적인 문제를 해결하는 방법의 예를 보여줍니다. 이 예제는 실질적이고 까다로운 문제를 어떻게 해결할 수 있는지 보여주는 간단한 예제로, 동적으로 변화하는 로드에 대응하여 리소스(예: 서버 또는 EC2 인스턴스)를 추가 및 제거하여 프로덕션 서비스를 확장합니다. 일별 및 주별 변형 및 간헐적 스파이크로 인위적 데이터를 생성하여 시뮬레이션 시스템을 생성합니다. 시뮬레이션된 시스템에는 새로운 리소스가 요청되는 시점과 요청을 서빙할 수 있는 시점 사이에 지연이 있습니다. 맞춤형 환경(environment)은 Open AI Gym을 사용하여 구성되며 한 에피소드에서 10000번의 타임스텝을 가집니다. 각 타임스텝에서 에이전트는 머신을 가감할 수 있습니다.

## Contents

* `rl_predictive_autoscaling_coach_customEnv.ipynb`: notebook used for training predictive auto-scaling policy.
* `src/`
  * `autoscalesim.py`: 사용자 정의 환경 및 시뮬레이터 정의
  * `gymhelper.py`: 사용자 정의 환경 및 시뮬레이터로부터 `gym.space.Box` 생성
  * `train-coach.py`: coach 훈련용 런처
  * `evaluate-coach.py`: coach 평가용 런처
  * `preset-autoscale-ppo.py`: Clipped PPO용 coach 프리셋
  * `preset-autoscale-a3c.py`: A3C용 coach 프리셋