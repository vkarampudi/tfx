# Copyright 2021 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A central place for feature name constants.

These names will be shared between the transform and the model.
"""

# import tensorflow as tf
# from tfx.examples.ranking import struct2tensor_parsing_utils

# Constants defining the label padding value and feature names
"""LABEL_PADDING_VALUE = -1
QUERY_TOKENS = 'query_tokens'
DOCUMENT_TOKENS = 'document_tokens'
LABEL = 'relevance'
LIST_SIZE_FEATURE_NAME = 'example_list_size'"""

# def get_features():
  """Defines the context features, example features, and label specifications for parsing.

  Returns:
    A tuple of three lists:
      - context_features: A list of features representing the context information.
      - example_features: A list of features representing the example information.
      - label: A feature representing the label.
  """

  # Define context features
  """context_features = [
      struct2tensor_parsing_utils.Feature(QUERY_TOKENS, tf.string)
  ]

  # Define example features
  example_features = [
      struct2tensor_parsing_utils.Feature(DOCUMENT_TOKENS, tf.string)
  ]

  # Define the label feature
  label = struct2tensor_parsing_utils.Feature(LABEL, tf.int64)

  return context_features, example_features, label"""
