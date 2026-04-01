from gemini import *

def run_basic_text_generation():
    answer = basic_text_generation("What is the capital of France?")    
    
    print('*'*50)

    print('generation of text example: \n')
    
    print('Type of answer: \n', type(answer))

    print('Core answer returns from endpoint: \n'+ str(answer))

    print('*'*50)

def run_text_generation_thinking():
    answer = text_generation_thinking("What is the capital of France?")    
    
    print('*'*50)

    print('generation of text with thinking process example: \n')
    
    print('Type of answer: \n', type(answer))

    print('Core answer returns from endpoint: \n'+ str(answer))

    print('*'*50)

def run_text_generation_with_system_prompts():
    answer = text_generation_with_system_prompts("What is your name?")    
    
    print('*'*50)

    print('generation of text with system prompts example: \n')
    
    print('Type of answer: \n', type(answer))

    print('Core answer returns from endpoint: \n'+ str(answer))

    print('*'*50)

def run_text_generation_with_dynamic_temprature(question):
    answer1 = text_generation_with_dynamic_temprature(question, 0.9)    
    answer2 = text_generation_with_dynamic_temprature(question, 0.1)

    print('*'*50)

    print('generation of text with dynamic temprature example: \n')
    
    print('Type of answer tmp=0.9: \n\n', (answer1.text))
    print('Type of answer tmp=0.1: \n\n', (answer2.text))

    print('*'*50)

def run_multimodel_input(question, path_of_image):
    answer = multimodel_input(question, path_of_image)

    print('*'*50)

    print('generation of text with multimodal input example: \n')

    print('Type of answer: \n', type(answer))

    print('Core answer returns from endpoint: \n'+ str(answer))

    print('*'*50)

if __name__ == "__main__":
    example_of_function_calling_2()