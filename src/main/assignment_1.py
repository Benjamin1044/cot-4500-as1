def DoublePrecision(input):

  s = 0
  c = 0
  f = 0
  max = len(input)  
  
  if input[0] == 1:
    s = 1

  for i in range(1,12):
    if input[i] == "1":
      hold = (11 - i)
      c += (2 ** hold) 
      
     
  for i in range(12,max):
    if input[i] == "1":
      temp = .5
      newhold = ( i - 11)
      f += (temp ** newhold)
      
  
  if s == 1:
    finalS = -1
  else:
    finalS = 1
  part1C = (c - 1023)
  finalC = (2 ** part1C)
  finalF = (1 + f)
  
  final = (float(finalS))*(float(finalC))*(finalF)

  print("{0:.5f}\n".format(final))
  return final

def chopping(final):
  qk = 10 ** 3
  chopped = (float(int(final * qk))/ qk)
  print(chopped,"\n")
 
def rounding(final):
  lk = 10 ** 3
  rounded = (float(int((final * lk) + .5))/ lk)
  print(rounded,"\n")
  return rounded
  
def absolute_error(final, rounded):

    sub_operation = final - rounded
    temp = abs(sub_operation)
    print(temp,"\n")
    return abs(sub_operation)

def relative_error(final, sub_operation):

    div_operation = sub_operation / final
    print(div_operation, "\n")
    

def check_for_alternating(function_we_got):
    term_check = check_for_negative_1_exponent_term(function_we_got)

    return term_check

def check_for_decreasing(function_we_got, x):
    decreasing_check = True
    k = 1
    starting_val = abs(eval(function_we_got))
    for k in range(2, x):
        result = abs(eval(function_we_got))

        print(result)
        if starting_val <= result:
            decreasing_check = False

    return decreasing_check


def check_for_negative_1_exponent_term(function) -> bool:
    if "-1**k" in function:
        return True

    return False


def use_minimum_term_function(error):
  count = 0
  while (  (1 + count) <= (10**(-1*(error/3))) ):
    count += 1

  print(count, "\n")


def  bisection_method(left, right, given_function, tolerance):

    
    diff = right - left

    iteration_counter = 0
    while (diff >= tolerance and iteration_counter <= 100):
        iteration_counter += 1

        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)

        if evaluated_midpoint == 0.0:
            break
      
        x = left
        evaluated_left_point = eval(given_function)
        
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0

        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)

    print(iteration_counter,"\n")


def custom_derivative(value):
    return (3 * value* value) + (8 * value)


def newton_raphson(initial_approximation, tolerance, sequence):
    
    iteration_counter = 0
    
    
    f = eval(sequence)
 
    f_prime = custom_derivative(initial_approximation)
    
    approximation = f / f_prime
    while(abs(approximation) >= tolerance):
       if eval(sequence) != 0: 
          x = initial_approximation
          f = eval(sequence)
          f_prime = custom_derivative(initial_approximation)
          approximation = f / f_prime
          if (abs(approximation) < tolerance):
              print(iteration_counter)
              return
        
          iteration_counter += 1
          initial_approximation -= approximation
        
    
  

if __name__ == "__main__":

  input = "010000000111111010111001000000000000000000000000000000"
   
  final = DoublePrecision(input)
  chopping(final)
  closetoFinal = rounding(final)
  sub_operation = absolute_error(final,closetoFinal)
  relative_error(final,sub_operation)
  
  function_a = "(-1**k) * (x**k) / (k**3)"
  x = 1
  check1: bool = check_for_alternating(function_a)
  check2: bool = check_for_decreasing(function_a, x)
  error = -4 

  if check1 and check2:
    use_minimum_term_function(error)
  left = -4
  right = 7
  function_string = "x**3 + (4*(x**2)) - 10"
  tolerance = 10**(-4)
  bisection_method(left, right, function_string, tolerance)

  both = right - left
  newton_raphson(both, tolerance, function_string)
 

   
