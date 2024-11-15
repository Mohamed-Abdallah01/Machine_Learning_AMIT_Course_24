
def gaussian_elimination(equations):
    # تحويل المعادلات إلى مصفوفة من المعاملات والثوابت
    matrix = [list(map(float, eq.split())) for eq in equations]
    n = len(matrix)
    
    # الحذف الغاوسي لتحويل المصفوفة إلى الشكل المثلثي العلوي
    for i in range(n):
        # جعل العنصر القطري يساوي 1
        divisor = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= divisor
        
        # جعل العناصر أسفل العنصر القطري تساوي 0
        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]
    
    # Back substitution لحساب قيم المتغيرات
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
    
    return solution