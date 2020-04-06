## Contextual Bandits with Parametric Actions - 실험 모드

이 예제는 Amazon SageMaker에서 contextual bandits 알고리즘으로 변동하는 행동(action) 개수에 대한 사용 예시를 보여줍니다. 예제 노트북 `bandits_movielens_testbed.ipynb`은 고정된 수의 행동들을 사용하는 [Contextual Bandits 예제 노트북]((https://github.com/awslabs/amazon-sagemaker-examples/blob/master/reinforcement_learning/bandits_statlog_vw_customEnv/bandits_statlog_vw_customEnv.ipynb))을 기반으로 합니다. Contextual bandits에 대한 기본적인 내용은 해당 노트북을 참조해 주세요.

Contextual bandit 설정에서 에이전트는 상태(state)가 주어진 행동을 추천합니다. 이 노트북에서는 좀 더 광범위한 실제 문제에 적용하기 위해 영화 추천 문제를 예시로 하여 세 가지의 추가 상황들을 나열해 보겠습니다.

1. 에이전트가 사용할 수있는 행동 개수는 시간이 지남에 따라 변경될 수 있습니다. 예를 들어, 카탈로그의 동영상들은 시간이 지남에 따라 변경됩니다.
2. 각 행동에는 관련 피처들이 있을 수 있습니다. 영화 추천 문제의 경우 각 영화에는 장르, 배우 등의 피처들이 있을 수 있습니다.
3. 에이전트는 행동/아이템의 랭크드(ranked) 리스트를 생성할 수 있습니다. 영화를 추천 할 때는 한 번에 여러 영화를 추천하는 것이 당연합니다.

Contextual bandit 에이전트는 exploitation와 exploration 사이의 균형을 유지하여, 사용자 선호도(user preferences)를 빠르게 배우고 좋지 않은 권장 항목들을 최소화합니다. Bandit 알고리즘은 카탈로그에 많은 콜드 항목(상호 작용 데이터가 없거나 거의 없는 항목)이 있거나 시간이 지남에 따라 사용자 기본 설정이 변경되는 경우 추천 문제에 사용하기에 적합합니다.


![Experimentation Workflow](workflow.png)