from abc import ABCMeta, abstractmethod


class Estimator(metaclass=ABCMeta):
    """Abstract base class for estimator.

    An estimator is the master class of all modeling operations. At minimum,
    it includes:

    1. input data and output data transformations (e.g. input image cropping,
    remove unused output labels...) when applicable.
    2. neural network graph (model) for either pytorch or tensorflow.
    3. procedures to execute model training and evaluation.

    One estimator could support multiple tasks (e.g. Mask R-CNN can be used for
    semantic segmentation and object detection)
    """

    @staticmethod
    def create(name, **kwargs):
        """Create a new instance of the estimators subclass

        Args:
            name (str): unique identifier for a estimators subclass
            config (dict): parameters specific to each estimators subclass
                used to create a estimators instance

        Returns:
            an instance of the specified estimators subclass
        """
        estimators_cls = Estimator.find(name)
        return estimators_cls(**kwargs)

    @staticmethod
    def find(name):
        """Find Estimator subclass based on the given name

        Args:
            name (str): unique identifier for a estimators subclass

        Returns:
            a label of the specified estimators subclass
        """
        estimators_classes = Estimator.__subclasses__()
        estimators_names = [e.__name__ for e in estimators_classes]
        if name in estimators_names:
            estimators_cls = estimators_classes[estimators_names.index(name)]
            return estimators_cls
        else:
            raise NotImplementedError(f"Unknown Estimator class {name}!")

    @abstractmethod
    def train(self, **kwargs):
        """Abstract method to train estimators
        """
        raise NotImplementedError("Subclass needs to implement this method")

    @abstractmethod
    def evaluate(self, **kwargs):
        """Abstract method to evaluate estimators
        """
        raise NotImplementedError("Subclass needs to implement this method")
