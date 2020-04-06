# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

def generate_s3_write_permission_for_sagemaker_role(role):
    role_name = role.split("/")[-1]
    url = "https://console.aws.amazon.com/iam/home#/roles/%s" % role_name
    text = "1. 현재 SageMaker 역할을 편집하려면 IAM 콘솔로 이동하세요.: [%s](%s).\n" % (role_name, url)
    text += "2. 다음으로 `Permissions tab`으로 이동하여 `Attach Policy`를 클릭하세요. \n"
    text += "3. `AmazonKinesisVideoStreamsFullAccess` 정책을 검색하고 선택하세요. \n"
    return text

def generate_kinesis_create_permission_for_sagemaker_role(role):
    role_name = role.split("/")[-1]
    url = "https://console.aws.amazon.com/iam/home#/roles/%s" % role_name
    text = "1. IAM 콘솔로 이동하여 현재 SageMaker 역할을 편집하세요.: [%s](%s).\n" % (role_name, url)
    text += "2. 다음으로 `Permissions tab` 으로 이동하여 `Attach Policy`를 클릭하세요. \n"
    text += "3. `AmazonS3FullAccess` 정책을 검색하고 선택하세요. \n"
    return text

def generate_help_for_s3_endpoint_permissions(role):
    role_name = role.split("/")[-1]
    url = "https://console.aws.amazon.com/iam/home#/roles/%s" % role_name
    text = "> SageMaker 역할에 권한이 충분하지 않은 것 같습니다. 다음을 수행해 주세요:\n"
    text += "1. IAM 콘솔로 이동하여 현재 SageMaker 역할을 편집하세요.: [%s](%s).\n" % (role_name, url)
    text += "2. %s 을 선택하고 `Edit Policy`를 클릭하세요. \n" % role_name
    text += "3. JSON 탭을 선택하고 다음 JSON Blob을 `Statement` 리스트에 추가하세요:\n"
    text += """```json
            {
            "Action": [
                "ec2:DescribeRouteTables",
                "ec2:CreateVpcEndpoint"
            ],
            "Effect": "Allow",
            "Resource": "*"
            },```\n"""
    text += "4. 이제 몇 분 동안 기다렸다가 이 셀을 다시 실행해 주세요."
    return text


def generate_help_for_robomaker_trust_relationship(role):
    role_name = role.split("/")[-1]
    url = "https://console.aws.amazon.com/iam/home#/roles/%s" % role_name
    text = "1. IAM 콘솔로 이동하여 현재 SageMaker 역할을 편집하세요.: [%s](%s).\n" % (role_name, url)
    text += "2. 그런 다음 `Trust relationships tab`으로 이동하여 `Edit Trust Relationship`을 클릭하세요. \n"
    text += "3. JSON Blob을 다음으로 변경합니다.:\n"
    text += """```json
            {
              "Version": "2012-10-17",
              "Statement": [
                {
                  "Effect": "Allow",
                  "Principal": {
                    "Service": [
                      "sagemaker.amazonaws.com",
                      "robomaker.amazonaws.com"
                    ]
                  },
                  "Action": "sts:AssumeRole"
                }
              ]
            }```\n"""
    text += "4. 완료 후, `Update Trust Policy`를 클릭하면 완료됩니다."
    return text


def generate_help_for_robomaker_all_permissions(role):
    role_name = role.split("/")[-1]
    url = "https://console.aws.amazon.com/iam/home#/roles/%s" % role_name
    text = "> SageMaker 역할에 권한이 충분하지 않은 것 같습니다. 다음을 수행해 주세요:\n"
    text += "1. IAM 콘솔로 이동하여 현재 SageMaker 역할을 편집하세요.: [%s](%s).\n" % (role_name, url)
    text += "2. `AmazonSageMaker-ExecutionPolicy`로 시작하는 정책을 클릭한 다음 정책을 편집하세요.\n"
    text += "3. JSON 탭을 선택하고 다음 JSON Blob을 `Statement` 리스트에 추가하고 정책을 저장하세요.:\n"
    text += """```json
        {
            "Effect": "Allow",
            "Action": [
                "robomaker:CreateSimulationApplication",
                "robomaker:DescribeSimulationApplication",
                "robomaker:DeleteSimulationApplication",
                "robomaker:CreateSimulationJob",
                "robomaker:DescribeSimulationJob",
                "robomaker:CancelSimulationJob",
                "robomaker:ListSimulationApplications"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": "robomaker.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "robomaker.amazonaws.com"
                    ]
                }
            }
        },```\n"""
    text += "4. 그런 다음 `Trust relationships tab`으로 이동하여 `Edit Trust Relationship`을 클릭하세요.\n"
    text += "5. 다음 JSON Blob을 `Statement` 리스트에 추가해 주세요.:\n"
    text += """```json
            {
              "Effect": "Allow",
              "Principal": {
                "Service": "robomaker.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
            },```\n"""
    text += "6. 이제 몇 분 동안 기다렸다가이 셀을 다시 실행해 주세요."
    return text


def generate_robomaker_links(job_arns, aws_region):
    simulation_ids = [job_arn.split("/")[-1] for job_arn in job_arns]
    robomaker_links = []
    for simulation_id in simulation_ids:
        robomaker_link = "https://%s.console.aws.amazon.com/robomaker/home?region=%s#simulationJobs/%s" % (aws_region,
                                                                                                           aws_region,
                                                                                                           simulation_id)
        robomaker_links.append(robomaker_link)

    markdown_content = '> RoboMaker Console에서 시뮬레이션 작업을 시각화하려면 다음 링크를 클릭해 주세요.\n'
    for i in range(len(robomaker_links)):
        markdown_content += "- [Simulation %s](%s)  \n" % (i + 1, robomaker_links[i])

    markdown_content += "\n위 링크를 연 후 Gazebo를 클릭하면 시뮬레이터를 시작할 수 있습니다."
    return markdown_content


def create_s3_endpoint_manually(aws_region, default_vpc):
    url = "https://%s.console.aws.amazon.com/vpc/home?region=%s#Endpoints:sort=vpcEndpointId" % (aws_region, aws_region)
    text = "> VPC S3 엔드포인트 생성에 실패했습니다. 엔드포인트를 수동으로 작성하려면 다음을 수행해 주세요.\n"
    text += "1. [VPC console | Endpoints](%s) 로 이동하세요\n" % url
    text += "2. `Create Endpoint`를 클릭하세요. `com.amazonaws.%s.s3` 형식의 서비스명을 선택하세요.\n" % (aws_region)
    text += "3. 그런 다음 기본 VPC: `%s'를 선택하고 기본 라우팅 테이블 ID에 대한 체크박스를 클릭하세요.\n" % (default_vpc)
    text += "4. 정책에서 `Full Access`를 선택한 다음 `Create Endpoint`를 클릭하세요. \n"
    text += "5. 이제 다음 셀로 진행하기 전에 몇 초 동안 기다려 주세요."
    return text


def generate_help_for_administrator_policy(role):
    role_name = role.split("/")[-1]
    url = "https://console.aws.amazon.com/iam/home#/roles/%s" % role_name
    text = "1. IAM 콘솔로 이동하여 현재 SageMaker 역할을 편집하세요.: [%s](%s).\n" % (role_name, url)
    text += "2. 그런 다음 `Permissions tab`으로 이동하여 `Attach policies`를 클릭하세요. \n"
    text += "3. `AdministratorAccess` 박스를 체크해 주세요. \n"
    text += "4. 아래에 있는 `Attach policy`를 클릭해 주세요. \n"
    text += "5. `Policy AdministratorAccess has been attached for the %s`" % (role) + "라는 메시지가 표시됩니다. \n"
    text += "6. 완료되면 모든 준비가 완료된 것입니다."
    return text

def generate_help_for_experiment_manager_permissions(role):
    role_name = role.split("/")[-1]
    url = "https://console.aws.amazon.com/iam/home#/roles/%s" % role_name
    text = "> SageMaker 역할에 권한이 충분하지 않은 것 같습니다. 다음을 수행해 주세요:\n"
    text += "1. IAM 콘솔로 이동하여 현재 SageMaker 역할을 편집하세요.: [%s](%s).\n" % (role_name, url)
    text += "2. `AmazonSageMaker-ExecutionPolicy`로 시작하는 정책을 클릭한 다음 정책을 편집하세요. \n"
    text += "3. JSON 탭을 선택하고 다음 JSON Blob을 `Statement` 리스트에 추가하고 정책을 저장하세요.:\n"
    
    text += """```json
        {
            "Effect": "Allow",
            "Action": [
                "firehose:*",
                "cloudformation:*",
                "dynamodb:*",
                "iam:*",
                "cloudwatch:*",
                "glue:*",
                "athena:*"
            ],
            "Resource": [
                "*"
            ]
        },```\n"""
    text += "4. 이제 이 셀을 다시 실행하기 전에 몇 분 동안 기다려 주세요."
    return text

