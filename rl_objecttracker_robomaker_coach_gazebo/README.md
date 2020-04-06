# Amazon SageMaker RL 및 RoboMaker를 사용한 객체 추적기(Object Tracker) RL 훈련

이 폴더에는 RL을 사용하여 Amazon SageMaker Reinforcement Learning 및 AWS RoboMaker를 사용하여 TurtleBot 객체 추적기를 훈련시키는 방법에 대한 예시가 포함되어 있습니다.

## Contents

* `rl_objecttracker_clippedppo_coach_tensorflow_robomaker.ipynb`: 객체 추적기를 훈련하는 노트북


* `src/`
  * `training_worker.py`: 분산 교육 작업을 시작하기 위한 기본 엔트리포인트
  * `robomaker/presets/object_tracker.py`: 객체 추적기의 프리셋(구성) 
  * `robomaker/environments/object_tracker_env.py`: 객체 추적기용 Gym 환경 파일
  * `markov/`: S3 업로드/다운로드를 위한 도우미 파일들
