# Amazon SageMaker RL 및 AWS RoboMaker 서비스를 사용하는 DeepRacer 노트북

이 폴더에는 RL을 사용하여 자율 딥레이서를 훈련시키는 방법의 예시가 포함되어 있습니다. 이 예제는 AWS DeepRacer의 jailbreak로, 이를 통해 DeepRacer를 작동시키는 데 사용되는 다양한 아키텍처를 확인할 수 있습니다.

## Contents

* `deepracer_rl.ipynb`: 자율 경주용 자동차 훈련을 위한 노트북 파일입니다.

* `Dockerfile`: SageMaker 기본 도커를 사용하는 대신 사용자 정의 도커를 사용합니다.

* `src/`
  * `training_worker.py`: 분산 훈련 작업을 시작하기 위한 기본 엔트리포인트
  * `markov/`: S3 업로드 및 다운로드를 위한 핼퍼 파일들
   * `presets/default.py`: Preset (configuration) for DeepRacer
   * `rewards/default.py`: 사용자 정의 보상 함수
   * `environments/deepracer_racetrack_env.py`: 딥레이서용 Gym 환경 파일
   * `actions/model_metadata_10_state.json`: 행동 공간(action space) 및 속도를 설정하는 JSON 파일
  * `lib/`: redis 구성 파일 및 ppo_head.py 사용자 정의 tensorflow 파일로 sagemaker 컨테이너에 복사됩니다.

* `common/`: 도커 파일들을 빌드하는 헬퍼 함수

## 노트북 사용법

1. AWS 계정에 로그인 후 - `SageMaker` 서비스를 선택합니다. ([SageMaker Link](https://us-west-2.console.aws.amazon.com/sagemaker/home?region=us-west-2#/dashboard))
2. 왼쪽 탭에서 `Notebook instances`를 선택하세요.
3. `Create notebook instance`을 선택하세요.
4. 노트북 인스턴스 이름을 기재하세요. 추가 구성에서 최소 25GB를 선택하세요. 도커가 설치되어 공간을 차지하기 때문입니다.
5. 새로운 IAM 역할을 생성하고 루트 권한을 부여해 주세요.
6. `git repository`를 선택하고 이 저장소를 복제하세요.
7. 그런 다음, 버튼에서 `create notebook instance` 버튼을 클릭하세요.
8. 노트북 인스턴스를 생성하는 데 2분 정도 걸립니다. 그런 다음, 신규 생성된 인스턴스를 클릭하고 juypter 노트북을 클릭하세요.
9. git repository에서 복제한 모든 github 파일들을 보실 수 있으며, 자율 자동차 훈련을 위해 `deepracer_rl.ipynb`을 실행하세요.
10. 훈련을 마친 경우에만 스크립트에서  robomaker 및 sagemaker 자원을 삭제하세요.

## DeepRacer 논문

AWS DeepRacer 기술 문서는 https://arxiv.org/abs/1911.01562 에서 확인할 수 있습니다. 다음은 인용을 위한 BibTeX 항목입니다.
```
@misc{deepracer2019,  
	title={DeepRacer: Educational Autonomous Racing Platform for Experimentation with Sim2Real Reinforcement Learning},
	author={Bharathan Balaji and Sunil Mallya and Sahika Genc and Saurabh Gupta and Leo Dirac and Vineet Khare and Gourav Roy and Tao Sun and Yunzhe Tao and Brian Townsend and Eddie Calleja and Sunil Muralidhara and Dhanasekar Karuppasamy},
	year={2019},  
	eprint={1911.01562},  
	archivePrefix={arXiv},  
	primaryClass={cs.LG}  
}
```
