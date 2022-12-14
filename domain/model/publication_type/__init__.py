from enum import Enum

from .alteration_license import AlterationLicense
from .animal_handling import AnimalHandling
from .cancel_ordinance import CancelOrdinance
from .condition_review import ConditionReview
from .environmental_authorization import EnvironmentalAuthorization
from .erratum import Erratum
from .exploration_approval import ExplorationApproval
from .extended_term import ExtendedTerm
from .forest_management import ForestManagement
from .forest_replacement_credit import ForestReplacementCredit
from .forest_volume_credit import ForestVolumeCredit
from .forest_volume_recognition import ForestVolumeRecognition
from .forest_volume_transfer import ForestVolumeTransfer
from .grant_waiver import GrantWaiver
from .installation_license import InstallationLicense
from .license_cancellation import LicenseCancellation
from .license_renewal import LicenseRenewal
from .license_revocation import LicenseRevocation
from .location_license import LocationLicense
from .operation_license import OperationLicense
from .owner_name_change import OwnerNameChange
from .ownership_transfer import OwnershipTransfer
from .planting_anticipation import PlantingAnticipation
from .preliminary_license import PreliminaryLicense
from .regularization_license import RegularizationLicense
from .right_use_water_resources import RightUseWaterResources
from .right_use_water_renovation import RightUseWaterResourcesRenovation
from .special_procedure import SpecialProcedure
from .unified_license import UnifiedLicense
from .vegetal_suppression import VegetalSuppression
from .owner_correction import OwnerCorrection
from .implantation_license import ImplantationLicense
from .infraction_warning import InfractionWarning
from .interdiction_infraction import InterdictionInfraction
from .demolition_penalty import DemolitionPenalty
from .fine_infraction import FineInfraction
from .seizure_infraction import SeizureInfraction
from .active_debt import ActiveDebit
from .grant_process import GrantProcess
from .process_extinction import ProcessExtinction
from .anticipated_environ_license import AnticipatedEnvironmentalLicense
from .notification_notice import NotificationNotice
from .simplified_environmental_license import SimplifiedEnvironmentalLicense
from .deadline_extension import DeadlineExtension
from .rectification import Rectification
from .order_revocation import OrderRevocation
from .seizure import Seizure
from .degraded_area_recovery_plan import DegradedAreaRecoveryPlan
from .grant_environmental_licenses import GrantEnvironmentalLicense
from .administrative_decision import AdministrativeDecision
from .conformity_certificate import ConformityCertificate
from .icmbio_infraction_notice import ICMBioInfractionNotice
from .ibama_infraction_notice import IbamaInfractionNotice

__all__ = [
    'AlterationLicense',
    'AnimalHandling',
    'CancelOrdinance',
    'ConditionReview',
    'EnvironmentalAuthorization',
    'Erratum',
    'ExplorationApproval',
    'ExtendedTerm',
    'ForestManagement',
    'ForestReplacementCredit',
    'ForestVolumeCredit',
    'ForestVolumeRecognition',
    'ForestVolumeTransfer',
    'GrantWaiver',
    'InstallationLicense',
    'LicenseCancellation',
    'LicenseRenewal',
    'LicenseRevocation',
    'LocationLicense',
    'OperationLicense',
    'OwnerNameChange',
    'OwnershipTransfer',
    'PlantingAnticipation',
    'PreliminaryLicense',
    'RegularizationLicense',
    'RightUseWaterResources',
    'RightUseWaterResourcesRenovation',
    'SpecialProcedure',
    'UnifiedLicense',
    'VegetalSuppression',
    'OwnerCorrection',
    'ImplantationLicense',
    'InfractionWarning',
    'InterdictionInfraction',
    'DemolitionPenalty',
    'FineInfraction',
    'SeizureInfraction',
    'ActiveDebit',
    'GrantProcess',
    'ProcessExtinction',
    'AnticipatedEnvironmentalLicense',
    'NotificationNotice',
    'SimplifiedEnvironmentalLicense',
    'DeadlineExtension',
    'Rectification',
    'OrderRevocation',
    'Seizure',
    'DegradedAreaRecoveryPlan',
    'GrantEnvironmentalLicense',
    'AdministrativeDecision',
    'ConformityCertificate',
    'ICMBioInfractionNotice',
    'IbamaInfractionNotice'
]


class PublicationType(Enum):
    ALTERATION_LICENSE = 'Licen??a de Altera????o'
    ANIMAL_HANDLING = 'Autoriza????o para Manejo de Fauna'
    CANCEL_ = 'Cancelamento'
    CONDITION_REVIEW = 'Revis??o de Condicionante'
    ENVIRONMENTAL_AUTHORIZATION = 'Autoriza????o Ambiental'
    ERRATUM = 'Errata'
    EXPLORATION_APPROVAL = 'Aprova????o da Explora????o ou Corte de Florestas Plantadas'  # noqa
    EXTENDED_TERM = 'Conceder Prorroga????o de Prazo de Validade'
    FOREST_MANAGEMENT = 'FOREST_MANAGEMENT'
    FOREST_REPLACEMENT_CREDIT = 'Emiss??o de Cr??dito de Reposi????o Florestal'
    FOREST_VOLUME_CREDIT = 'Emiss??o de Cr??dito Florestal'
    FOREST_VOLUME_RECOGNITION = 'Reconhecimento de Volume Florestal'
    FOREST_VOLUME_TRANSFER = 'Transfer??ncia de Cr??dito de Volume Florestal'
    GRANT_WAIVER = 'GRANT_WAIVER'
    INSTALLATION_LICENSE = 'Licen??a de Instala????o'
    LICENSE_CANCELLATION = 'Cancelamento de Licen??a'
    LICENSE_RENEWAL = 'Renova????o de Licen??a'
    LICENSE_REVOCATION = 'Revoga????o de Licen??a'
    OPERATION_LICENSE = 'Licen??a de Opera????o'
    OWNER_NAME_CHANGE = 'Altera????o da Raz??o Social'
    OWNERSHIP_TRANSFER = 'Transfer??ncia de Titularidade'
    PLANTING_ANTICIPATION = 'Antecipacao de Plantio'
    PRELIMINARY_LICENSE = 'PRELIMINARY_LICENSE'
    REGULARIZATION_LICENSE = 'Licen??a de Regulariza????o'
    RIGHT_USE_WATER_RESOURCES = 'Outorga do Direito de Uso dos Recursos H??dricos'  # noqa
    SPECIAL_PROCEDURE = 'Autoriza????o por Procedimento Especial'
    UNIFIED_LICENSE = 'Licen??a Unificada'
    VEGETAL_SUPPRESSION = 'Autoriza????o de Supress??o de Vegeta????o Nativa'
    LOCATION_LICENSE = 'Licen??a de Localiza????o'
    OWNER_CORRECTION = 'Ret??fica da Raz??o Social'
    IMPLANTATION_LICENSE = 'Licen??a de Implanta????o'
    INFRACTION_WARNING = 'Auto de Infra????o de Advert??ncia'
    INTERDICTION_INFRACTION = 'Embargo e Interdi????o'
    DEMOLITION_PENALTY = 'Auto de Infra????o de Interdi????o'
    FINE_INFRACTION = 'Auto de Infra????o de Multa'
    SEIZURE_INFRACTION = 'Auto de Infra????o de Apreens??o'
    ACTIVE_DEBIT = 'D??vida Ativa'
    GRANT_PROCESS = 'An??lise de Processo de Outorga'
    PROCESS_EXTINCTION = 'Extin????o de Processo'
    ANTICIPATED_ENVIRONMENTAL_LICENSE = ''
    NOTIFICATION_NOTICE = 'Licen??a Ambiental Pr??vial'
    SIMPLIFIED_ENVIRONMENTAL_LICENSE = 'Licen??a Simplificada'
    DEADLINE_EXTENSION = 'Prorroga????o de Prazo de Validade'
    RECTIFICATION = 'Retifica????o de Portaria'
    ORDER_REVOCATION = 'Revoga????o Licen??a'
    SEIZURE = 'Interdi????o'
    DEGRADED_AREA_RECOVERY_PLAN = 'Plano de Recupera????o de ??rea Degradada'
    GRANT_ENVIRONMENTAL_LICENSE = 'GRANT_ENVIRONMENTAL_LICENSE'
    ADMINISTRATIVE_DECISION = 'Decis??o Administrativa'
    CONFORMITY_CERTIFICATE = 'Certid??o de Conformidade de Uso e Ocupa????o do Solo'  # noqa
    ICMBIO_INFRACTION_NOTICE = 'Autos de Infra????o Emitidos pelo ICMBio'
    IBAMA_INFRACTION_NOTICE = 'Autos de Infra????o Emitidos Pelo IBAMA'
    LICENSE_DISMISSAL = 'Dispensa de Licen??a Ambiental'
    LEGAL_RESERVE_LOCATION_APPROVAL = 'Aprova????o de Localiza????o de Reserva Legal'  # noqa
    TEMPORARY_INTERDICTION_NOTICE = 'Auto de Infra????o de Interdi????o Tempor??ria'  # noqa
    PROCESS_ANALYSIS = 'An??lise de Processo'
    PLANT_ENRICHMENT_PLAN = 'Plano de Enriquecimento Vegetal'
    TEMPORARY_SEIZURE = 'Embargo Tempor??rio'
    PENALTY_WARNING = 'Penalidade de Advert??ncia'
    CEFIR = 'Cadastro Estadual Florestal de Im??veis Rurais'
    SOLID_WASTE_MANAGEMENT_PLAN = 'Programa de Gerenciamento de Res??duos S??lidos'  # noqa
    RIGHT_USE_WATER_RESOURCES_RENOVATION = 'Renova????o da Outorga do Direito de Uso dos Recursos H??dricos'  # noqa
    RIGHT_USE_WATER_RESOURCES_CHANGE = 'Altera????o da Outorga do Direito de Uso dos Recursos H??dricos'  # noqa
    VOLUME_EXPASION = 'Amplia????o do volume'
    PREVENTIVE = 'Preventiva'
    TEMPORARY_SUSPEND = 'Suspender Temporariamente'
