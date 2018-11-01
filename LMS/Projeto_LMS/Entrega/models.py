from django.db import models

class Professor(models.Model):
    login = models.CharField("Login", max_length=50)
    senha = models.CharField("Senha", max_length=50)
    nome = models.CharField("Nome", max_length=100)
    email = models.CharField("Email", max_length=100)
    celular = models.CharField("Celular", max_length=20)
    dt_expiracao = models.DateField("Data Expiracao", max_length=10)
    apelido = models.CharField("Apelido", max_length=25)

    def __str__(self):
        return self.login

class Alunos(models.Model):
    login = models.CharField("Login", max_length=50)
    senha = models.CharField("Senha", max_length=50)
    nome = models.CharField("Nome", max_length=100)
    email = models.CharField("Email", max_length=100)
    celular = models.CharField("Celular", max_length=20)
    dt_expiracao = models.DateField("Data Expiracao", max_length=10)
    ra = models.CharField("RA", max_length=7)
    foto = models.CharField("Foto", null=True, blank=True, max_length=100)

    def __str__(self):
        return self.login

class Entrega(models.Model):
    titulo = models.CharField("Titulo", max_length=50)
    resposta = models.CharField("Resposta", max_length=50)
    DtEntrega = models.DateField("DtEntrega", max_length=10)
    Status = models.CharField("Status", max_length=50)
    Nota = models.DecimalField("Nota",max_digits=5, decimal_places=2)
    DtAvaliacao = models.DateField("DtAvaliacao", max_length=10)
    Obs = models.CharField("Obs", max_length=50)
    Professor = models.ForeignKey("Professor", on_delete=models.CASCADE)
    Aluno = models.ForeignKey("Aluno", on_delete=models.CASCADE)
    AtividadeVinculada = models.ForeignKey("AtividadeVinculada", on_delete=models.CASCADE)
	
    def __str__(self):
        return self.Aluno
