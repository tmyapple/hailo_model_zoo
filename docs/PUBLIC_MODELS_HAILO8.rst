Public Pre-Trained Models
=========================

.. |rocket| image:: images/rocket.png
  :width: 18

.. |star| image:: images/star.png
  :width: 18

Here, we give the full list of publicly pre-trained models supported by the Hailo Model Zoo.

* Network available in `Hailo Benchmark <https://hailo.ai/developer-zone/benchmarks/>`_ are marked with |rocket|
* Networks available in `TAPPAS <https://hailo.ai/developer-zone/tappas-apps-toolkit/>`_ are marked with |star|
* Benchmark, TAPPAS and Recommended networks run in performance mode
* All models were compiled using Hailo Dataflow Compiler v3.26.0
* Supported tasks:

  * `Classification`_
  * `Object Detection`_

.. _Classification:

Classification
--------------

ImageNet
^^^^^^^^

.. list-table::
   :widths: 31 9 7 11 9 8 8 8 7 7 7
   :header-rows: 1

   * - Network Name
     - Accuracy (top1)
     - Quantized
     - Input Resolution (HxWxC)
     - Params (M)
     - OPS (G)
     - Pretrained
     - Source
     - Compiled
     - FPS (Batch Size=1)
     - FPS (Batch Size=8)
   * - efficientnet_l
     - 80.46
     - 79.36
     - 300x300x3
     - 10.55
     - 19.4
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/efficientnet_l/pretrained/2023-07-18/efficientnet_l.zip>`_
     - `link <https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/efficientnet_l.hef>`_
     - 155.208
     - 155.208
   * - efficientnet_lite0
     - 74.99
     - 73.81
     - 224x224x3
     - 4.63
     - 0.78
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/efficientnet_lite0/pretrained/2023-07-18/efficientnet_lite0.zip>`_
     - `link <https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/efficientnet_lite0.hef>`_
     - 1731.95
     - 1731.94
   * - efficientnet_lite1
     - 76.68
     - 76.21
     - 240x240x3
     - 5.39
     - 1.22
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/efficientnet_lite1/pretrained/2023-07-18/efficientnet_lite1.zip>`_
     - `link <https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/efficientnet_lite1.hef>`_
     - 934.714
     - 934.709
   * - efficientnet_lite2
     - 77.45
     - 76.74
     - 260x260x3
     - 6.06
     - 1.74
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/efficientnet_lite2/pretrained/2023-07-18/efficientnet_lite2.zip>`_
     - `link <https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/efficientnet_lite2.hef>`_
     - 433.436
     - 433.435
   * - efficientnet_lite3
     - 79.29
     - 78.33
     - 280x280x3
     - 8.16
     - 2.8
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/efficientnet_lite3/pretrained/2023-07-18/efficientnet_lite3.zip>`_
     - `link <https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/efficientnet_lite3.hef>`_
     - 223.849
     - 223.848
   * - efficientnet_lite4
     - 80.79
     - 79.99
     - 300x300x3
     - 12.95
     - 5.10
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/efficientnet_lite4/pretrained/2023-07-18/efficientnet_lite4.zip>`_
     - `link <https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/efficientnet_lite4.hef>`_
     - 301.62
     - 301.619
   * - efficientnet_m |rocket|
     - 78.91
     - 78.63
     - 240x240x3
     - 6.87
     - 7.32
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/efficientnet_m/pretrained/2023-07-18/efficientnet_m.zip>`_
     - `link <https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/efficientnet_m.hef>`_
     - 890.529
     - 890.53
   * - efficientnet_s
     - 77.64
     - 77.32
     - 224x224x3
     - 5.41
     - 4.72
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/efficientnet_s/pretrained/2023-07-18/efficientnet_s.zip>`_
     - `link <https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/efficientnet_s.hef>`_
     - 1036.47
     - 1036.47
   * - hardnet39ds
     - 73.43
     - 72.92
     - 224x224x3
     - 3.48
     - 0.86
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/hardnet39ds/pretrained/2021-07-20/hardnet39ds.zip>`_
     - `link <https://github.com/PingoLH/Pytorch-HarDNet>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/hardnet39ds.hef>`_
     - 328.985
     - 1348.15
   * - hardnet68
     - 75.47
     - 75.04
     - 224x224x3
     - 17.56
     - 8.5
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/hardnet68/pretrained/2021-07-20/hardnet68.zip>`_
     - `link <https://github.com/PingoLH/Pytorch-HarDNet>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/hardnet68.hef>`_
     - 122.727
     - 347.067
   * - inception_v1
     - 69.74
     - 69.54
     - 224x224x3
     - 6.62
     - 3
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/inception_v1/pretrained/2023-07-18/inception_v1.zip>`_
     - `link <https://github.com/tensorflow/models/tree/v1.13.0/research/slim>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/inception_v1.hef>`_
     - 928.649
     - 928.906
   * - mobilenet_v1
     - 70.97
     - 70.26
     - 224x224x3
     - 4.22
     - 1.14
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/mobilenet_v1/pretrained/2023-07-18/mobilenet_v1.zip>`_
     - `link <https://github.com/tensorflow/models/tree/v1.13.0/research/slim>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/mobilenet_v1.hef>`_
     - 3489.37
     - 3489.35
   * - mobilenet_v2_1.0 |rocket|
     - 71.78
     - 71.0
     - 224x224x3
     - 3.49
     - 0.62
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/mobilenet_v2_1.0/pretrained/2021-07-11/mobilenet_v2_1.0.zip>`_
     - `link <https://github.com/tensorflow/models/tree/v1.13.0/research/slim>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/mobilenet_v2_1.0.hef>`_
     - 2443.67
     - 2443.68
   * - mobilenet_v2_1.4
     - 74.18
     - 73.18
     - 224x224x3
     - 6.09
     - 1.18
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/mobilenet_v2_1.4/pretrained/2021-07-11/mobilenet_v2_1.4.zip>`_
     - `link <https://github.com/tensorflow/models/tree/v1.13.0/research/slim>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/mobilenet_v2_1.4.hef>`_
     - 1676.77
     - 1676.7
   * - mobilenet_v3
     - 72.21
     - 71.73
     - 224x224x3
     - 4.07
     - 2
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/mobilenet_v3/pretrained/2023-07-18/mobilenet_v3.zip>`_
     - `link <https://github.com/tensorflow/models/tree/master/research/slim/nets/mobilenet>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/mobilenet_v3.hef>`_
     - 2488.59
     - 2488.52
   * - mobilenet_v3_large_minimalistic
     - 72.11
     - 70.96
     - 224x224x3
     - 3.91
     - 0.42
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/mobilenet_v3_large_minimalistic/pretrained/2021-07-11/mobilenet_v3_large_minimalistic.zip>`_
     - `link <https://github.com/tensorflow/models/tree/master/research/slim/nets/mobilenet>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/mobilenet_v3_large_minimalistic.hef>`_
     - 3484.95
     - 3485.62
   * - regnetx_1.6gf
     - 77.05
     - 76.75
     - 224x224x3
     - 9.17
     - 3.22
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/regnetx_1.6gf/pretrained/2021-07-11/regnetx_1.6gf.zip>`_
     - `link <https://github.com/facebookresearch/pycls>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/regnetx_1.6gf.hef>`_
     - 2321.66
     - 2321.6
   * - regnetx_800mf
     - 75.16
     - 74.84
     - 224x224x3
     - 7.24
     - 1.6
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/regnetx_800mf/pretrained/2021-07-11/regnetx_800mf.zip>`_
     - `link <https://github.com/facebookresearch/pycls>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/regnetx_800mf.hef>`_
     - 3506.03
     - 3506.02
   * - repvgg_a1
     - 74.4
     - 72.4
     - 224x224x3
     - 12.79
     - 4.7
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/repvgg/repvgg_a1/pretrained/2022-10-02/RepVGG-A1.zip>`_
     - `link <https://github.com/DingXiaoH/RepVGG>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/repvgg_a1.hef>`_
     - 2545.65
     - 2545.64
   * - repvgg_a2
     - 76.52
     - 74.52
     - 224x224x3
     - 25.5
     - 10.2
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/repvgg/repvgg_a2/pretrained/2022-10-02/RepVGG-A2.zip>`_
     - `link <https://github.com/DingXiaoH/RepVGG>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/repvgg_a2.hef>`_
     - 911.79
     - 911.784
   * - resmlp12_relu
     - 75.26
     - 74.32
     - 224x224x3
     - 15.77
     - 6.04
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/resmlp12_relu/pretrained/2022-03-03/resmlp12_relu.zip>`_
     - `link <https://github.com/rwightman/pytorch-image-models/>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/resmlp12_relu.hef>`_
     - 1430.06
     - 1429.99
   * - resnet_v1_18
     - 71.26
     - 71.06
     - 224x224x3
     - 11.68
     - 3.64
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/resnet_v1_18/pretrained/2022-04-19/resnet_v1_18.zip>`_
     - `link <https://github.com/yhhhli/BRECQ>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/resnet_v1_18.hef>`_
     - 2533.72
     - 2533.78
   * - resnet_v1_34
     - 72.7
     - 72.14
     - 224x224x3
     - 21.79
     - 7.34
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/resnet_v1_34/pretrained/2021-07-11/resnet_v1_34.zip>`_
     - `link <https://github.com/tensorflow/models/tree/master/research/slim>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/resnet_v1_34.hef>`_
     - 1346.63
     - 1346.62
   * - resnet_v1_50 |rocket| |star|
     - 75.12
     - 74.47
     - 224x224x3
     - 25.53
     - 6.98
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/resnet_v1_50/pretrained/2021-07-11/resnet_v1_50.zip>`_
     - `link <https://github.com/tensorflow/models/tree/master/research/slim>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/resnet_v1_50.hef>`_
     - 1331.76
     - 1331.76
   * - resnext26_32x4d
     - 76.18
     - 75.78
     - 224x224x3
     - 15.37
     - 4.96
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/resnext26_32x4d/pretrained/2023-09-18/resnext26_32x4d.zip>`_
     - `link <https://github.com/osmr/imgclsmob/tree/master/pytorch>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/resnext26_32x4d.hef>`_
     - 1630.58
     - 1630.58
   * - resnext50_32x4d
     - 79.31
     - 78.21
     - 224x224x3
     - 24.99
     - 8.48
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/resnext50_32x4d/pretrained/2023-07-18/resnext50_32x4d.zip>`_
     - `link <https://github.com/osmr/imgclsmob/tree/master/pytorch>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/resnext50_32x4d.hef>`_
     - 398.117
     - 398.05
   * - squeezenet_v1.1
     - 59.85
     - 59.4
     - 224x224x3
     - 1.24
     - 0.78
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/squeezenet_v1.1/pretrained/2023-07-18/squeezenet_v1.1.zip>`_
     - `link <https://github.com/osmr/imgclsmob/tree/master/pytorch>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/squeezenet_v1.1.hef>`_
     - 3035.18
     - 3035.17
   * - vit_base_bn
     - 79.98
     - 78.58
     - 224x224x3
     - 86.5
     - 34.25
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/vit_base/pretrained/2023-01-25/vit_base.zip>`_
     - `link <https://github.com/rwightman/pytorch-image-models>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/vit_base_bn.hef>`_
     - 34.5985
     - 126.352
   * - vit_small_bn
     - 78.12
     - 77.02
     - 224x224x3
     - 21.12
     - 8.62
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/vit_small/pretrained/2022-08-08/vit_small.zip>`_
     - `link <https://github.com/rwightman/pytorch-image-models>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/vit_small_bn.hef>`_
     - 120.661
     - 559.253
   * - vit_tiny_bn
     - 68.95
     - 66.75
     - 224x224x3
     - 5.73
     - 2.2
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Classification/vit_tiny/pretrained/2023-08-29/vit_tiny_bn.zip>`_
     - `link <https://github.com/rwightman/pytorch-image-models>`_
     - `download <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.10.0/hailo8/vit_tiny_bn.hef>`_
     - 204.19
     - 1092.91

.. _Object Detection:

Object Detection
----------------

COCO
^^^^

.. list-table::
   :widths: 33 8 7 12 8 8 8 7 7
   :header-rows: 1

   * - Network Name
     - mAP
     - Quantized
     - Input Resolution (HxWxC)
     - Params (M)
     - MAC (G)
     - Pretrained
     - Source
     - Compiled
   * - centernet_resnet_v1_18_postprocess
     - 26.29
     - 24.16
     - 512x512x3
     - 14.22
     - 15.63
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/centernet/centernet_resnet_v1_18/pretrained/2021-07-11/centernet_resnet_v1_18.zip>`_
     - `link <https://cv.gluon.ai/model_zoo/detection.html>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/centernet_resnet_v1_18_postprocess.hef>`_
   * - centernet_resnet_v1_50_postprocess
     - 31.78
     - 29.64
     - 512x512x3
     - 30.07
     - 28.46
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/centernet/centernet_resnet_v1_50_postprocess/pretrained/2021-07-11/centernet_resnet_v1_50_postprocess.zip>`_
     - `link <https://cv.gluon.ai/model_zoo/detection.html>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/centernet_resnet_v1_50_postprocess.hef>`_
   * - damoyolo_tinynasL20_T
     - 42.8
     - 42.0
     - 640x640x3
     - 11.35
     - 9.03
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/damoyolo_tinynasL20_T/pretrained/2022-12-19/damoyolo_tinynasL20_T.zip>`_
     - `link <https://github.com/tinyvision/DAMO-YOLO>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/damoyolo_tinynasL20_T.hef>`_
   * - damoyolo_tinynasL25_S
     - 46.53
     - 46.04
     - 640x640x3
     - 16.25
     - 18.85
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/damoyolo_tinynasL25_S/pretrained/2022-12-19/damoyolo_tinynasL25_S.zip>`_
     - `link <https://github.com/tinyvision/DAMO-YOLO>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/damoyolo_tinynasL25_S.hef>`_
   * - damoyolo_tinynasL35_M
     - 49.7
     - 47.23
     - 640x640x3
     - 33.98
     - 30.87
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/damoyolo_tinynasL35_M/pretrained/2022-12-19/damoyolo_tinynasL35_M.zip>`_
     - `link <https://github.com/tinyvision/DAMO-YOLO>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/damoyolo_tinynasL35_M.hef>`_
   * - efficientdet_lite0
     - 27.43
     - 26.6
     - 320x320x3
     - 3.56
     - 0.99
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/efficientdet/efficientdet_lite0/pretrained/2022-06-14/efficientdet-lite0.zip>`_
     - `link <https://github.com/google/automl/tree/master/efficientdet>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/efficientdet_lite0.hef>`_
   * - efficientdet_lite1
     - 32.46
     - 31.91
     - 384x384x3
     - 4.73
     - 2
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/efficientdet/efficientdet_lite1/pretrained/2022-06-26/efficientdet-lite1.zip>`_
     - `link <https://github.com/google/automl/tree/master/efficientdet>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/efficientdet_lite1.hef>`_
   * - efficientdet_lite2
     - 36.16
     - 34.88
     - 448x448x3
     - 5.93
     - 3.42
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/efficientdet/efficientdet_lite2/pretrained/2022-06-26/efficientdet-lite2.zip>`_
     - `link <https://github.com/google/automl/tree/master/efficientdet>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/efficientdet_lite2.hef>`_
   * - nanodet_repvgg
     - 29.3
     - 28.53
     - 416x416x3
     - 6.74
     - 5.64
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/nanodet/nanodet_repvgg/pretrained/2022-02-07/nanodet.zip>`_
     - `link <https://github.com/RangiLyu/nanodet>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/nanodet_repvgg.hef>`_
   * - nanodet_repvgg_a1_640
     - 33.28
     - 32.88
     - 640x640x3
     - 10.79
     - 21.4
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/nanodet/nanodet_repvgg_a1_640/pretrained/2022-07-19/nanodet_repvgg_a1_640.zip>`_
     - `link <https://github.com/RangiLyu/nanodet>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/nanodet_repvgg_a1_640.hef>`_
   * - ssd_mobilenet_v1 |rocket| |star|
     - 23.17
     - 22.37
     - 300x300x3
     - 6.79
     - 1.25
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/ssd/ssd_mobilenet_v1/pretrained/2021-07-11/ssd_mobilenet_v1.zip>`_
     - `link <https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/ssd_mobilenet_v1.hef>`_
   * - ssd_mobilenet_v1_hd
     - 17.66
     - 15.73
     - 720x1280x3
     - 6.81
     - 12.26
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/ssd/ssd_mobilenet_v1_hd/pretrained/2021-07-11/ssd_mobilenet_v1_hd.zip>`_
     - `link <https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/ssd_mobilenet_v1_hd.hef>`_
   * - ssd_mobilenet_v2
     - 24.15
     - 23.07
     - 300x300x3
     - 4.46
     - 0.76
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/ssd/ssd_mobilenet_v2/pretrained/2021-07-11/ssd_mobilenet_v2.zip>`_
     - `link <https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/ssd_mobilenet_v2.hef>`_
   * - tiny_yolov3
     - 14.36
     - 14.16
     - 416x416x3
     - 8.85
     - 2.79
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/tiny_yolov3/pretrained/2021-07-11/tiny_yolov3.zip>`_
     - `link <https://github.com/Tianxiaomo/pytorch-YOLOv4>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/tiny_yolov3.hef>`_
   * - tiny_yolov4
     - 19.18
     - 17.73
     - 416x416x3
     - 6.05
     - 3.46
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/tiny_yolov4/pretrained/2021-07-11/tiny_yolov4.zip>`_
     - `link <https://github.com/Tianxiaomo/pytorch-YOLOv4>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/tiny_yolov4.hef>`_
   * - yolov3  |star|
     - 38.42
     - 37.32
     - 608x608x3
     - 68.79
     - 79.17
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov3/pretrained/2021-08-16/yolov3.zip>`_
     - `link <https://github.com/AlexeyAB/darknet>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov3.hef>`_
   * - yolov3_416
     - 37.73
     - 36.08
     - 416x416x3
     - 61.92
     - 32.97
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov3_416/pretrained/2021-08-16/yolov3_416.zip>`_
     - `link <https://github.com/AlexeyAB/darknet>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov3_416.hef>`_
   * - yolov3_gluon |rocket| |star|
     - 37.28
     - 35.64
     - 608x608x3
     - 68.79
     - 79.17
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov3_gluon/pretrained/2021-07-11/yolov3_gluon.zip>`_
     - `link <https://cv.gluon.ai/model_zoo/detection.html>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov3_gluon.hef>`_
   * - yolov3_gluon_416  |star|
     - 36.27
     - 34.92
     - 416x416x3
     - 61.92
     - 32.97
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov3_gluon_416/pretrained/2021-07-11/yolov3_gluon_416.zip>`_
     - `link <https://cv.gluon.ai/model_zoo/detection.html>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov3_gluon_416.hef>`_
   * - yolov4_leaky  |star|
     - 42.37
     - 41.47
     - 512x512x3
     - 64.33
     - 45.60
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov4/pretrained/2022-03-17/yolov4.zip>`_
     - `link <https://github.com/AlexeyAB/darknet/wiki/YOLOv4-model-zoo>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov4_leaky.hef>`_
   * - yolov5l
     - 46.01
     - 44.01
     - 640x640x3
     - 48.54
     - 60.78
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov5l_spp/pretrained/2022-02-03/yolov5l.zip>`_
     - `link <https://github.com/ultralytics/yolov5/releases/tag/v2.0>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5l.hef>`_
   * - yolov5m
     - 42.59
     - 41.19
     - 640x640x3
     - 21.78
     - 26.14
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov5m_spp/pretrained/2022-01-02/yolov5m.zip>`_
     - `link <https://github.com/ultralytics/yolov5/releases/tag/v2.0>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5m.hef>`_
   * - yolov5m6_6.1
     - 50.68
     - 48.74
     - 1280x1280x3
     - 35.70
     - 100.02
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov5m6_6.1/pretrained/2022-04-12/yolov5m6.zip>`_
     - `link <https://github.com/ultralytics/yolov5/releases/tag/v6.1>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5m6_6.1.hef>`_
   * - yolov5m_6.1
     - 44.81
     - 43.38
     - 640x640x3
     - 21.17
     - 24.48
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov5m_6.1/pretrained/2022-03-24/yolov5m_6.1.zip>`_
     - `link <https://github.com/ultralytics/yolov5/releases/tag/v6.1>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5m_6.1.hef>`_
   * - yolov5m_hpp
     - 42.59
     - 41.19
     - 640x640x3
     - 21.78
     - 26.14
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov5m_spp/pretrained/2022-01-02/yolov5m.zip>`_
     - `link <https://github.com/ultralytics/yolov5/releases/tag/v2.0>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5m_hpp.hef>`_
   * - yolov5m_wo_spp |rocket|
     - 42.46
     - 40.43
     - 640x640x3
     - 22.67
     - 26.49
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov5m/pretrained/2022-04-19/yolov5m_wo_spp.zip>`_
     - `link <https://github.com/ultralytics/yolov5/releases/tag/v2.0>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5m_wo_spp_60p.hef>`_
   * - yolov5n6_6.1
     - 35.63
     - 33.68
     - 1280x1280x3
     - 3.24
     - 9.17
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov5n6_6.1/pretrained/2022-04-12/yolov5n6.zip>`_
     - `link <https://github.com/ultralytics/yolov5/releases/tag/v6.1>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5n6_6.1.hef>`_
   * - yolov5s  |star|
     - 35.33
     - 34.25
     - 640x640x3
     - 7.46
     - 8.72
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov5s_spp/pretrained/2022-01-02/yolov5s.zip>`_
     - `link <https://github.com/ultralytics/yolov5/releases/tag/v2.0>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5s.hef>`_
   * - yolov5s6_6.1
     - 44.17
     - 41.74
     - 1280x1280x3
     - 12.61
     - 33.70
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov5s6_6.1/pretrained/2022-04-12/yolov5s6.zip>`_
     - `link <https://github.com/ultralytics/yolov5/releases/tag/v6.1>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5s6_6.1.hef>`_
   * - yolov5s_c3tr
     - 37.13
     - 35.33
     - 640x640x3
     - 10.29
     - 8.51
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov5s_c3tr/pretrained/2023-02-07/yolov5s_c3tr.zip>`_
     - `link <https://github.com/ultralytics/yolov5/tree/v6.0>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5s_c3tr.hef>`_
   * - yolov5xs_wo_spp
     - 32.78
     - 31.8
     - 512x512x3
     - 7.85
     - 5.68
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov5xs/pretrained/2021-07-11/yolov5xs.zip>`_
     - `link <https://github.com/ultralytics/yolov5/releases/tag/v2.0>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5xs_wo_spp.hef>`_
   * - yolov5xs_wo_spp_nms
     - 32.57
     - 31.06
     - 512x512x3
     - 7.85
     - 5.68
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov5xs/pretrained/2022-05-10/yolov5xs_wo_spp_nms.zip>`_
     - `link <https://github.com/ultralytics/yolov5/releases/tag/v2.0>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5xs_wo_spp_nms.hef>`_
   * - yolov6n
     - 34.29
     - 32.19
     - 640x640x3
     - 4.32
     - 5.57
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov6n/pretrained/2022-06-28/yolov6n.zip>`_
     - `link <https://github.com/meituan/YOLOv6/releases/tag/0.1.0>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov6n.hef>`_
   * - yolov7
     - 49.72
     - 46.92
     - 640x640x3
     - 36.91
     - 52.34
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov7/pretrained/2022-07-10/yolov7.zip>`_
     - `link <https://github.com/WongKinYiu/yolov7>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov7.hef>`_
   * - yolov7_tiny
     - 36.49
     - 35.39
     - 640x640x3
     - 6.22
     - 6.87
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov7_tiny/pretrained/2022-07-10/yolov7_tiny.zip>`_
     - `link <https://github.com/WongKinYiu/yolov7>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov7_tiny.hef>`_
   * - yolov7e6
     - 55.37
     - 53.17
     - 1280x1280x3
     - 97.20
     - 257.56
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov7e6/pretrained/2022-10-19/yolov7-e6.zip>`_
     - `link <https://github.com/WongKinYiu/yolov7>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov7e6.hef>`_
   * - yolov8l
     - 52.61
     - 51.95
     - 640x640x3
     - 43.7
     - 82.65
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov8l/2023-02-02/yolov8l.zip>`_
     - `link <https://github.com/ultralytics/ultralytics>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov8l.hef>`_
   * - yolov8m
     - 50.08
     - 49.28
     - 640x640x3
     - 25.9
     - 39.5
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov8m/2023-02-02/yolov8m.zip>`_
     - `link <https://github.com/ultralytics/ultralytics>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov8m.hef>`_
   * - yolov8n
     - 37.23
     - 36.23
     - 640x640x3
     - 3.2
     - 4.4
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov8n/2023-01-30/yolov8n.zip>`_
     - `link <https://github.com/ultralytics/ultralytics>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov8n.hef>`_
   * - yolov8s
     - 44.75
     - 44.15
     - 640x640x3
     - 11.2
     - 14.3
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov8s/2023-02-02/yolov8s.zip>`_
     - `link <https://github.com/ultralytics/ultralytics>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov8s.hef>`_
   * - yolov8x
     - 53.61
     - 52.21
     - 640x640x3
     - 68.2
     - 129
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolov8x/2023-02-02/yolov8x.zip>`_
     - `link <https://github.com/ultralytics/ultralytics>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov8x.hef>`_
   * - yolox_l_leaky  |star|
     - 48.68
     - 47.08
     - 640x640x3
     - 54.17
     - 77.74
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolox_l_leaky/pretrained/2021-09-23/yolox_l_leaky.zip>`_
     - `link <https://github.com/Megvii-BaseDetection/YOLOX>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolox_l_leaky.hef>`_
   * - yolox_s_leaky
     - 38.13
     - 37.51
     - 640x640x3
     - 8.96
     - 13.37
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolox_s_leaky/pretrained/2021-09-12/yolox_s_leaky.zip>`_
     - `link <https://github.com/Megvii-BaseDetection/YOLOX>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolox_s_leaky.hef>`_
   * - yolox_s_wide_leaky
     - 42.4
     - 41.38
     - 640x640x3
     - 20.12
     - 29.73
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolox_s_wide_leaky/pretrained/2021-09-12/yolox_s_wide_leaky.zip>`_
     - `link <https://github.com/Megvii-BaseDetection/YOLOX>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolox_s_wide_leaky.hef>`_
   * - yolox_tiny
     - 32.64
     - 31.32
     - 416x416x3
     - 5.05
     - 3.22
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-COCO/yolo/yolox/yolox_tiny/pretrained/2022-06-01/yolox_tiny.zip>`_
     - `link <https://github.com/Megvii-BaseDetection/YOLOX>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolox_tiny.hef>`_

VisDrone
^^^^^^^^

.. list-table::
   :widths: 31 7 9 12 9 8 9 8 7
   :header-rows: 1

   * - Network Name
     - mAP
     - Quantized
     - Input Resolution (HxWxC)
     - Params (M)
     - MAC (G)
     - Pretrained
     - Source
     - Compiled
   * - ssd_mobilenet_v1_visdrone  |star|
     - 2.18
     - 2.16
     - 300x300x3
     - 5.64
     - 1.15
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ObjectDetection/Detection-Visdrone/ssd/ssd_mobilenet_v1_visdrone/pretrained/2021-07-11/ssd_mobilenet_v1_visdrone.zip>`_
     - `link <https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/ssd_mobilenet_v1_visdrone.hef>`_

.. _Semantic Segmentation:

Semantic Segmentation
---------------------

Cityscapes
^^^^^^^^^^

.. list-table::
   :widths: 31 7 9 12 9 8 9 8 7
   :header-rows: 1

   * - Network Name
     - mIoU
     - Quantized
     - Input Resolution (HxWxC)
     - Params (M)
     - MAC (G)
     - Pretrained
     - Source
     - Compiled
   * - fcn16_resnet_v1_18  |star|
     - 66.83
     - 66.39
     - 1024x1920x3
     - 11.19
     - 71.26
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Segmentation/Cityscapes/fcn16_resnet_v1_18/pretrained/2022-02-07/fcn16_resnet_v1_18.zip>`_
     - `link <https://mmsegmentation.readthedocs.io/en/latest>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/fcn16_resnet_v1_18.hef>`_
   * - fcn8_resnet_v1_18
     - 68.75
     - 67.97
     - 1024x1920x3
     - 11.20
     - 71.51
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Segmentation/Cityscapes/fcn8_resnet_v1_18/pretrained/2022-02-09/fcn8_resnet_v1_18.zip>`_
     - `link <https://mmsegmentation.readthedocs.io/en/latest>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/fcn8_resnet_v1_18.hef>`_
   * - fcn8_resnet_v1_22
     - 67.55
     - 67.39
     - 1024x1920x3
     - 15.12
     - 150.04
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Segmentation/Cityscapes/fcn8_resnet_v1_22/pretrained/2021-07-11/fcn8_resnet_v1_22.zip>`_
     - `link <https://cv.gluon.ai/model_zoo/segmentation.html>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/fcn8_resnet_v1_22.hef>`_
   * - stdc1 |rocket|
     - 74.57
     - 73.47
     - 1024x1920x3
     - 8.27
     - 63.34
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Segmentation/Cityscapes/stdc1/pretrained/2022-03-17/stdc1.zip>`_
     - `link <https://mmsegmentation.readthedocs.io/en/latest>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/stdc1.hef>`_

Oxford-IIIT Pet
^^^^^^^^^^^^^^^

.. list-table::
   :widths: 31 7 9 12 9 8 9 8 7
   :header-rows: 1

   * - Network Name
     - mIoU
     - Quantized
     - Input Resolution (HxWxC)
     - Params (M)
     - MAC (G)
     - Pretrained
     - Source
     - Compiled
   * - unet_mobilenet_v2
     - 77.32
     - 77.02
     - 256x256x3
     - 10.08
     - 14.44
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Segmentation/Oxford_Pet/unet_mobilenet_v2/pretrained/2022-02-03/unet_mobilenet_v2.zip>`_
     - `link <https://www.tensorflow.org/tutorials/images/segmentation>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/unet_mobilenet_v2.hef>`_

Pascal VOC
^^^^^^^^^^

.. list-table::
   :widths: 36 7 9 12 9 8 9 8 7
   :header-rows: 1

   * - Network Name
     - mIoU
     - Quantized
     - Input Resolution (HxWxC)
     - Params (M)
     - MAC (G)
     - Pretrained
     - Source
     - Compiled
   * - deeplab_v3_mobilenet_v2
     - 76.05
     - 74.8
     - 513x513x3
     - 2.10
     - 8.91
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Segmentation/Pascal/deeplab_v3_mobilenet_v2_dilation/pretrained/2021-09-26/deeplab_v3_mobilenet_v2_dilation.zip>`_
     - `link <https://github.com/bonlime/keras-deeplab-v3-plus>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/deeplab_v3_mobilenet_v2.hef>`_
   * - deeplab_v3_mobilenet_v2_wo_dilation
     - 71.46
     - 71.08
     - 513x513x3
     - 2.10
     - 1.64
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/Segmentation/Pascal/deeplab_v3_mobilenet_v2/pretrained/2021-08-12/deeplab_v3_mobilenet_v2.zip>`_
     - `link <https://github.com/tensorflow/models/tree/master/research/deeplab>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/deeplab_v3_mobilenet_v2_wo_dilation.hef>`_

.. _Pose Estimation:

Pose Estimation
---------------

COCO
^^^^

.. list-table::
   :widths: 24 8 9 18 9 8 9 8 7
   :header-rows: 1

   * - Network Name
     - AP
     - Quantized
     - Input Resolution (HxWxC)
     - Params (M)
     - MAC (G)
     - Pretrained
     - Source
     - Compiled
   * - centerpose_regnetx_1.6gf_fpn  |star|
     - 53.54
     - 47.65
     - 640x640x3
     - 14.28
     - 32.38
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/PoseEstimation/centerpose_regnetx_1.6gf_fpn/pretrained/2022-03-23/centerpose_regnetx_1.6gf_fpn.zip>`_
     - `link <https://github.com/tensorboy/centerpose>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/centerpose_regnetx_1.6gf_fpn.hef>`_
   * - centerpose_regnetx_800mf
     - 44.07
     - 41.9
     - 512x512x3
     - 12.31
     - 43.06
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/PoseEstimation/centerpose_regnetx_800mf/pretrained/2021-07-11/centerpose_regnetx_800mf.zip>`_
     - `link <https://github.com/tensorboy/centerpose>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/centerpose_regnetx_800mf.hef>`_
   * - centerpose_repvgg_a0  |star|
     - 39.17
     - 37.09
     - 416x416x3
     - 11.71
     - 14.15
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/PoseEstimation/centerpose_repvgg_a0/pretrained/2021-09-26/centerpose_repvgg_a0.zip>`_
     - `link <https://github.com/tensorboy/centerpose>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/centerpose_repvgg_a0.hef>`_

.. _Single Person Pose Estimation:

Single Person Pose Estimation
-----------------------------

COCO
^^^^

.. list-table::
   :widths: 24 8 9 18 9 8 9 8 7
   :header-rows: 1

   * - Network Name
     - AP
     - Quantized
     - Input Resolution (HxWxC)
     - Params (M)
     - MAC (G)
     - Pretrained
     - Source
     - Compiled
   * - mspn_regnetx_800mf
     - 70.8
     - 70.3
     - 256x192x3
     - 7.17
     - 1.47
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/SinglePersonPoseEstimation/mspn_regnetx_800mf/pretrained/2022-07-12/mspn_regnetx_800mf.zip>`_
     - `link <https://github.com/open-mmlab/mmpose>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/mspn_regnetx_800mf.hef>`_

.. _Face Detection:

Face Detection
--------------

WiderFace
^^^^^^^^^

.. list-table::
   :widths: 24 7 12 11 9 8 8 8 7
   :header-rows: 1

   * - Network Name
     - mAP
     - Quantized
     - Input Resolution (HxWxC)
     - Params (M)
     - MAC (G)
     - Pretrained
     - Source
     - Compiled
   * - lightface_slim  |star|
     - 39.7
     - 39.41
     - 240x320x3
     - 0.26
     - 0.08
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/FaceDetection/lightface_slim/2021-07-18/lightface_slim.zip>`_
     - `link <https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/lightface_slim.hef>`_
   * - retinaface_mobilenet_v1  |star|
     - 81.27
     - 81.17
     - 736x1280x3
     - 3.49
     - 12.57
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/FaceDetection/retinaface_mobilenet_v1_hd/2021-07-18/retinaface_mobilenet_v1_hd.zip>`_
     - `link <https://github.com/biubug6/Pytorch_Retinaface>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/retinaface_mobilenet_v1.hef>`_
   * - scrfd_10g
     - 82.13
     - 82.03
     - 640x640x3
     - 4.23
     - 13.37
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/FaceDetection/scrfd/scrfd_10g/pretrained/2022-09-07/scrfd_10g.zip>`_
     - `link <https://github.com/deepinsight/insightface>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/scrfd_10g.hef>`_
   * - scrfd_2.5g
     - 76.59
     - 76.32
     - 640x640x3
     - 0.82
     - 3.44
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/FaceDetection/scrfd/scrfd_2.5g/pretrained/2022-09-07/scrfd_2.5g.zip>`_
     - `link <https://github.com/deepinsight/insightface>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/scrfd_2.5g.hef>`_
   * - scrfd_500m
     - 68.98
     - 68.88
     - 640x640x3
     - 0.63
     - 0.75
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/FaceDetection/scrfd/scrfd_500m/pretrained/2022-09-07/scrfd_500m.zip>`_
     - `link <https://github.com/deepinsight/insightface>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/scrfd_500m.hef>`_

.. _Instance Segmentation:

Instance Segmentation
---------------------

COCO
^^^^

.. list-table::
   :widths: 34 7 7 11 9 8 8 8 7
   :header-rows: 1

   * - Network Name
     - mAP-segmentation
     - Quantized
     - Input Resolution (HxWxC)
     - Params (M)
     - MAC (G)
     - Pretrained
     - Source
     - Compiled
   * - yolact_mobilenet_v1
     - 14.98
     - 14.86
     - 512x512x3
     - 19.11
     - 51.92
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/InstanceSegmentation/coco/yolact_mobilenet_v1/pretrained/2021-01-12/yolact_mobilenet_v1.zip>`_
     - `link <https://github.com/dbolya/yolact>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolact_mobilenet_v1.hef>`_
   * - yolact_regnetx_1.6gf
     - 27.57
     - 27.27
     - 512x512x3
     - 30.09
     - 62.67
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/InstanceSegmentation/coco/yolact_regnetx_1.6gf/pretrained/2022-11-30/yolact_regnetx_1.6gf.zip>`_
     - `link <https://github.com/dbolya/yolact>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolact_regnetx_1.6gf.hef>`_
   * - yolact_regnetx_800mf
     - 25.61
     - 25.5
     - 512x512x3
     - 28.3
     - 58.375
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/InstanceSegmentation/coco/yolact_regnetx_800mf/pretrained/2022-11-30/yolact_regnetx_800mf.zip>`_
     - `link <https://github.com/dbolya/yolact>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolact_regnetx_800mf.hef>`_
   * - yolact_regnetx_800mf_20classes  |star|
     - 20.23
     - 20.22
     - 512x512x3
     - 21.97
     - 51.47
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/InstanceSegmentation/coco/yolact_regnetx_800mf/pretrained/2022-11-30/yolact_regnetx_800mf.zip>`_
     - `link <https://github.com/dbolya/yolact>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolact_regnetx_800mf_20classes.hef>`_
   * - yolov5l_seg
     - 39.78
     - 39.09
     - 640x640x3
     - 47.89
     - 73.94
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/InstanceSegmentation/coco/yolov5/yolov5l/pretrained/2022-10-30/yolov5l-seg.zip>`_
     - `link <https://github.com/ultralytics/yolov5>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5l_seg.hef>`_
   * - yolov5m_seg
     - 37.05
     - 36.32
     - 640x640x3
     - 32.60
     - 35.47
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/InstanceSegmentation/coco/yolov5/yolov5m/pretrained/2022-10-30/yolov5m-seg.zip>`_
     - `link <https://github.com/ultralytics/yolov5>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5m_seg.hef>`_
   * - yolov5n_seg
     - 23.35
     - 22.24
     - 640x640x3
     - 1.99
     - 3.55
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/InstanceSegmentation/coco/yolov5/yolov5n/pretrained/2022-10-30/yolov5n-seg.zip>`_
     - `link <https://github.com/ultralytics/yolov5>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5n_seg.hef>`_
   * - yolov5s_seg
     - 31.57
     - 30.49
     - 640x640x3
     - 7.61
     - 13.21
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/InstanceSegmentation/coco/yolov5/yolov5s/pretrained/2022-10-30/yolov5s-seg.zip>`_
     - `link <https://github.com/ultralytics/yolov5>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolov5s_seg.hef>`_

D2S
^^^

.. list-table::
   :widths: 34 7 7 11 9 8 8 8 7
   :header-rows: 1

   * - Network Name
     - mAP-segmentation
     - Quantized
     - Input Resolution (HxWxC)
     - Params (M)
     - MAC (G)
     - Pretrained
     - Source
     - Compiled
   * - yolact_regnetx_600mf_d2s_31classes
     - 62.48
     - 63.36
     - 512x512x3
     - 22.14
     - 51.62
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/InstanceSegmentation/d2s/yolact_regnetx_600mf/pretrained/2022-07-19/yolact_regnetx_600mf_d2s.zip>`_
     - `link <https://github.com/dbolya/yolact>`_
     - `link <https://hailo-model-zoo.s3.eu-west-2.amazonaws.com/ModelZoo/Compiled/v2.7.0/yolact_regnetx_600mf_d2s_31classes.hef>`_
