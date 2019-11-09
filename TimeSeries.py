import pandas as pd
import matplotlib.pyplot as plt


class TimeSeries:
    
    def __init__(self, dfName):
        self.dfName = dfName
        self.df = pd.read_csv(self.dfName, sep = ',', header=[0], encoding="latin1")
        
        
    def convertIncomeGroupsToMoney(self, df1, df2):
        pass

    def getSubset(self, gender, age, state):
        # filtering with query method 
        subset = self.df.query('Sexo == @gender and Grupo_edad == @age and Entidad_Federativa == @state') 
        #subset = self.df.query(Sexo == gender and Grupo_edad == age and Entidad_Federativa == state) 
        return subset #['Nivel_ingreso','Periodo']
        #sal_df['Nivel_ingreso'].unique()

    def ploter(self, gender, age, state):
        print( gender + " " + age + " " + state)
        subset = self.getSubset(gender, age, state)
        subset.plot(kind='scatter',x='Periodo', y='Nivel_ingreso', color='red')
        plt.show()
        
        
if __name__ == '__main__':
    #
    procTimeSeries = TimeSeries("Poblacion_Subordinada_Nivel_Ingresos.csv")
    #procTimeSeries.ploter('Hombre', 'M\xa0s de 3 hasta 5 s.m.', 'Michoacan')
    #print ( procTimeSeries.getSubset('Hombre', 'M\xa0s de 3 hasta 5 s.m.', 'Jalisco') )
    print ( procTimeSeries.getSubset('Hombre', 'Menos de 1 s.m.', 'Jalisco') )
