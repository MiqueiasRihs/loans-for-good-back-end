class EnumMaritalStatusOptions(object):
    NONE = 1
    SINGLE = 2
    MARRIED = 3
    DIVORCED = 4
    WIDOWED = 5
    
class EnumAnalysisStatus(object):
    APPROVED = 1
    DENIED = 2
    
ANALYSIS_STATUS = (
    (EnumAnalysisStatus.APPROVED, u'Aprovado'),
    (EnumAnalysisStatus.DENIED, u'Negado'),
)

MARITAL_STATUS_OPTIONS = (
    (EnumMaritalStatusOptions.NONE, u' --- '),
    (EnumMaritalStatusOptions.SINGLE, u'Solteiro'),
    (EnumMaritalStatusOptions.MARRIED, u'Casado'),
    (EnumMaritalStatusOptions.DIVORCED, u'Divorciado'),
    (EnumMaritalStatusOptions.WIDOWED, u'Viúvo')
)

FIELD_OPTIONS = [
    ('email', 'Email'),
    ('marital_status', 'Status civil'),
    ('birth_date', 'Data de aniversário'),
    ('nationality', 'Nacionalidade'),
    ('phone_number', 'Telefone'),
    ('monthly_income', 'Renda mensal'),
]


FIELD_OPTIONS_DICT = {
    'email': {
        'name': 'email',
        'type': 'text',
        'label': 'Email',
        'placeholder': 'Digite seu email',
    },
    'marital_status': {
        'name': 'marital_status',
        'type': 'select',
        'label': 'Status civil',
        'placeholder': 'Qual seu estado civil',
        'options': [{key: value} for key, value in MARITAL_STATUS_OPTIONS]
    },
    'birth_date': {
        'name': 'birth_date',
        'type': 'text',
        'label': 'Data de aniversário',
        'placeholder': 'Digite seu aniversário',
    },
    'nationality': {
        'name': 'nationality',
        'type': 'text',
        'label': 'Nacionalidade',
        'placeholder': 'Digite sua nacionalidade',
    },
    'phone_number': {
        'name': 'phone_number',
        'type': 'text',
        'label': 'Telefone',
        'placeholder': 'Digite seu telefone',
    },
    'monthly_income': {
        'name': 'monthly_income',
        'type': 'number',
        'label': 'Renda mensal',
        'placeholder': 'Digite sua renda mensal',
    },
}


def document_validation(document):
    if len(document) != 11:
        return False

    # Calculate the first verification digit.
    soma = 0
    for i in range(9):
        soma += int(document[i]) * (10 - i)
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(document[9]):
        return False

    # Calculates the second verification digit
    soma = 0
    for i in range(10):
        soma += int(document[i]) * (11 - i)
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(document[10]):
        return False

    return True