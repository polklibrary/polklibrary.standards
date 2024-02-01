# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import polklibrary.standards


class PolklibraryStandardsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=polklibrary.standards)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'polklibrary.standards:default')


POLKLIBRARY_STANDARDS_FIXTURE = PolklibraryStandardsLayer()


POLKLIBRARY_STANDARDS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(POLKLIBRARY_STANDARDS_FIXTURE,),
    name='PolklibraryStandardsLayer:IntegrationTesting',
)


POLKLIBRARY_STANDARDS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(POLKLIBRARY_STANDARDS_FIXTURE,),
    name='PolklibraryStandardsLayer:FunctionalTesting',
)


POLKLIBRARY_STANDARDS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        POLKLIBRARY_STANDARDS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PolklibraryStandardsLayer:AcceptanceTesting',
)
