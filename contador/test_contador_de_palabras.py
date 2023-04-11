import unittest
from contador_de_palabras import contadordepalabras
class Testclase3comp(unittest.TestCase):
    def test_hola(self):
        resultado = contadordepalabras('hola')
        self.assertEqual(resultado, {'hola':1})
    def test_hola_(self):
        resultado = contadordepalabras('hola_')
        self.assertEqual(resultado, {'hola':1})
    def test_hola_(self):
        resultado = contadordepalabras('hola CHAU HOLA chau')
        self.assertEqual(resultado, {'hola':2, 'chau':2} )
    def test_SeParar_los_programas_de_los_TEST(self):
        resultado = contadordepalabras('SeParar los programas de los TEST')
        self.assertEqual(resultado, {'los':2, 'separar':1, 'de':1, 'test':1, 'programas':1} )
    def test_la_oracion_no_tiene_coherencia(self):
        resultado = contadordepalabras('la oracion no tiene coherencia')
        self.assertEqual(resultado, {'la':1, 'oracion':1, 'no':1,'tiene':1, 'coherencia':1} )
    def test_este_test_TENDRIA_que_andar_correctamente(self):
        resultado = contadordepalabras('este test TENDRIA andar correctamente')
        self.assertEqual(resultado, {'este':1, 'test':1, 'tendria':1,'andar':1, 'correctamente':1} )
    def test_si_sI_Si_SI_NO_NO_NO_NO(self):
        resultado = contadordepalabras('si sI Si SI NO NO NO NO')
        self.assertEqual(resultado, {'si':4, 'no':4} )
if __name__ == '__main__':
    unittest.main()
