class EnumMaritalStatusOptions(object):
    SINGLE = 1
    MARRIED = 2
    DIVORCED = 3
    WIDOWED = 4
    
MARITAL_STATUS_OPTIONS = (
    (EnumMaritalStatusOptions.SINGLE, u'Solteiro'),
    (EnumMaritalStatusOptions.MARRIED, u'Casado'),
    (EnumMaritalStatusOptions.DIVORCED, u'Divorciado'),
    (EnumMaritalStatusOptions.WIDOWED, u'Viúvo')
)

FIELD_OPTIONS = [
    ('name', 'Nome'),
    ('document', 'Documento'),
    ('email', 'Email'),
    ('marital_status', 'Status civil'),
    ('birth_date', 'Data de aniversário'),
    ('nationality', 'Nacionalidade'),
    ('phone_number', 'Telefone'),
    ('monthly_income', 'Renda mensal'),
]
