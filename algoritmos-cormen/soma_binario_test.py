import unittest
import soma_binario

class TestSomaBinario(unittest.TestCase):
    def setUp(self):
        self.a = [1, 0, 0, 1, 1]
        self.b = [0, 1, 0, 1, 0]
        
    def test_soma(self):
        self.assertEqual(soma_binario.soma(self.a, self.b), [1, 1, 1, 0, 1])

    def test_table(self):
        for i in range(17):
            for j in range(17):
                # print(i, j)
                self.assertEqual(soma_binario.soma(soma_binario.dec_to_bin(i), soma_binario.dec_to_bin(j)), soma_binario.dec_to_bin(i + j))

    def test_binlst(self):
        c = [1, 0, 1, 1]  # 11
        d = [0, 1, 1, 1]  # 7
        self.assertEqual(soma_binario.binlst_to_dec(soma_binario.soma(c, d)), 18)
        
if __name__ == "__main__":
    unittest.main()
