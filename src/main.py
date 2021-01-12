# from module import <class name>
from src.elections import Elections

if __name__ == '__main__':
    elect = Elections()
    #elect.run_model()
    elect.run_rigged_model("Independent")

