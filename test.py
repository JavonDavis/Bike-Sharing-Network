import numpy as np

inputs = np.array([[0.5, -0.2, 0.1]])
targets = np.array([[0.4]])
test_w_i_h = np.array([[0.1, -0.2],
                       [0.4, 0.5],
                       [-0.3, 0.2]])
test_w_h_o = np.array([[0.3],
                       [-0.1]])

final_w_h_o = np.array([[ 0.37275328],[-0.03172939]])

final_w_i_h = np.array([[ 0.10562014, -0.20185996],
                        [0.39775194, 0.50074398],
                        [-0.29887597, 0.19962801]])
lr = 0.5
n_records = inputs.shape[0]

hidden_inputs = np.dot(inputs,test_w_i_h)
hidden_outputs = 1/(1+np.exp(-hidden_inputs))

final_inputs = np.dot(hidden_outputs,test_w_h_o)
final_outputs = final_inputs

print('hidden_inputs',hidden_inputs)
print('hidden_outputs',hidden_outputs)
print('final_inputs',final_inputs)
print('final_outputs',final_outputs)

delta_weights_h_o = n_records*(final_w_h_o - test_w_h_o)/lr

delta_weights_i_h = n_records*(final_w_i_h - test_w_i_h)/lr

print('delta_weights_h_o',delta_weights_h_o)
print('delta_weights_i_h',delta_weights_i_h)

error = (targets - final_outputs)

print ('error',error)

output_error_term = error*final_outputs*(1-final_outputs)

print('output_error_term',output_error_term)

delta_output = output_error_term*hidden_outputs

print ('delta_output',delta_output)

test = delta_weights_h_o[0]/hidden_outputs[0]

print('test', test)

test1 = test

print('test1',test1)

testerror = - targets*np.log(final_outputs) - (1 - targets) * np.log(1-final_outputs)

print('testerror',testerror)
