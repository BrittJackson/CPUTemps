#! /usr/bin/env python3
'''
Created on June 9, 2021

@author: bnjac

Performs gaussian elimination to find the solution for 
the system of equations of temperatures and time steps for each core
'''
import numpy as np

def arrangeMatrix(core0, core1, core2, core3, step_size):
    
    """
    Arranges the XTX matrix

    Args:     
        core0, core1, core2, core3: Temp data for each core
        
        step_size: Time intervals in seconds        
    """
    
    #add ones to step size list and arrange into two columns
    x_Matrix = np.vstack([np.ones(len(step_size)), step_size])
    x_Matrix = np.transpose(x_Matrix)

    x_Transpose = np.transpose(x_Matrix)
    xTx = multiply(x_Transpose, x_Matrix)
    
    #arrange temperatures vertically for Y values
    core0 = np.vstack(core0)
    core1 = np.vstack(core1)
    core2 = np.vstack(core2)
    core3 = np.vstack(core3)
    
    core_list = [core0, core1, core2, core3]
    
    getMatrixValues(x_Transpose, xTx, core_list, step_size)

def getMatrixValues(x_Transpose, xTx, core_list, step_size):
    
    """
    Iterates over each core matrix to be solved

    Args:     
        x_Tranpose: The X matrix (of time intervals) transposed
        
        xTx: The matrix resulting from multiplying X matrix by X transposed
        
        core_list: list of four cores
        
        step_size: Time intervals in seconds       
    """
    core = 0
    
    for i, val in enumerate(core_list):
        xTy = multiply(x_Transpose, val)  
        xTy = np.delete(xTy,1, 1)
        core_matrix = np.hstack([xTx,xTy])
        eliminate(core_matrix, xTx, xTy)
        backSolve(core_matrix, xTx, xTy, step_size[0],step_size[-1], core)
        core +=1

def multiply(lhs, rhs):
    """
    Performs matrix multiplication

    Args:
        lhs: Matrix 'A'

        rhs: Matrix 'B' to be multiplied by matrix 'A'

    Returns:
        Matrix resulting from two matrices multiplied
    """
    xTx_xTy = [[0,0],[0,0]]
    
    for i in range(len(lhs)):
        for j in range(len(rhs[0])):
            for k in range(len(rhs)):
                xTx_xTy[i][j] += lhs[i][k] * rhs[k][j]

    xTx_xTy = np.reshape(xTx_xTy, (2,2))
    
    return xTx_xTy

def swap(xtx_xty):
    """
    Swaps largest and smallest matrix rows

    Args:
        xtx_xty: The matrix (X transposed X | X Transposed Y)
        
    Returns:
        Matrix with rows swapped
    """
    matrix_dim = xtx_xty.shape[0]
    
    for i in range(matrix_dim - 1):
        k = i
        for j in range(i + 1, matrix_dim):
            if xtx_xty[j][i] > xtx_xty[k][i]:
                xtx_xty[(k,j ), :] = xtx_xty[(j, k), :]
                return  xtx_xty      
                
def eliminate(xtx_xty, xTx, xTy):   
    """
    Eliminates rows in matrix

    Args:
        xtx_xty: The matrix (X transposed X | X Transposed Y)
        
        xTx: The matrix X transposed * matrix X
        
        xTy: The matrix X transposed * matrix Y
        
    Returns:
        Row Echelon Form Matrix
    """
    matrix_dim = xtx_xty.shape[0] 
    quotient = []
    
    for i in range(0, matrix_dim-1):
        swap(xtx_xty)
        for j in range(i + 1, matrix_dim):
            quotient = np.divide(xtx_xty[i,:], xtx_xty[j,i])
            xtx_xty[j] = xtx_xty[i,:] - quotient[i] * xtx_xty[j]
    
    return xtx_xty

def backSolve(xtx_xty, xTx, xTy, x1, xn, core):
    """
    Solves matrix and determines coefficients 

    Args:
        xtx_xty: The matrix (X transposed X | X Transposed Y)        
        
        xTx: The matrix X transposed * matrix X        
        
        xTy: The matrix X transposed * matrix Y       
        
        x1: Starting time interval for temperature      
         
        xn: Ending time interval for temperature
        
        core: The core for which the operations are being performed (i.e. core 0, 1, 2, or 3)
    """
    matrix_dim = xtx_xty.shape[0] 

    for i in range(matrix_dim-1, -1, -1):
        xtx_xty[i,:] /= xtx_xty[i, i]
        for j in range(i-1, -1, -1):
            mult = xtx_xty[i,i] / xtx_xty[j,i]
            xtx_xty[j] = xtx_xty[i,:] - mult * xtx_xty[j]
    
    coeff_val = xtx_xty[:,2]
    coeff_val[0] = np.format_float_positional(np.float16(coeff_val[0]))
    coeff_val[1] = np.format_float_positional(np.float16(coeff_val[1]))
   
    writeCoeff_toFile(x1, xn, coeff_val, core)

def writeCoeff_toFile(x1, xn, coefficients, core):
    """
    Writes the least squares approximation to its respective core file

    Args:
        x1: Starting time step for temperature
        xn: Ending time step for temperature
        core: The core for which the operations are being performed (i.e. core 0, 1, 2, or 3)
    """
    if core == 0:
        f = open("cpuTemps-core-0.txt",'+a')
        f.write(str(x1)+" <=x< "+str(xn)+"; "+" y= "+str(coefficients[0])+" + "+ " " +str(coefficients[1])+"x; " + " " + "  least squares"+"\n")
        f.close()
            
    elif core == 1:
        f = open("cpuTemps-core-1.txt",'+a')
        f.write(str(x1)+" <=x< "+str(xn)+"; "+" y= "+str(coefficients[0])+" + "+ " " +str(coefficients[1])+"x; " + " " + "  least squares"+"\n")
        f.close()
           
    elif core == 2:
        f = open("cpuTemps-core-2.txt",'+a')
        f.write(str(x1)+" <=x< "+str(xn)+"; "+" y= "+str(coefficients[0])+" + "+ " " +str(coefficients[1])+"x; " + " " + "  least squares"+"\n")
        f.close()
            
    elif core == 3:
        f = open("cpuTemps-core-3.txt",'+a')
        f.write(str(x1)+" <=x< "+str(xn)+"; "+" y= "+str(coefficients[0])+" + "+ " " +str(coefficients[1])+"x; " + " " + "  least squares"+"\n")
        f.close()      
