
class GenericFormation():
    formationManager = None
    employeeManager = None

    def __init__(self, Formation, Employee) -> None:
        self.formationManager = Formation
        self.employeeManager = Employee

    def add_formation(self, request):
        employee = self.employeeManager.objects.get(id=request.data['trabalhador'])

        formation = self.formationManager.objects.create(
            trabalhador = employee,
            formacao = request.data['formacao'],
            validity = request.data['validity']
        )
    
        return formation

