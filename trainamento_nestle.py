import dlib
import time
opcoes = dlib.simple_object_detector_training_options()
opcoes.add_left_right_image_flips = True
opcoes.C = 5

inicio = time.time()
dlib.train_simple_object_detector("Grades/3_imglab.xml", "Grades/imglab.svm", opcoes)
fim = time.time()
print(fim - inicio)