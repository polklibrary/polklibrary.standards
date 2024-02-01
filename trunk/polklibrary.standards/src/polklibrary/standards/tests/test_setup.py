# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from polklibrary.standards.testing import POLKLIBRARY_STANDARDS_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that polklibrary.standards is properly installed."""

    layer = POLKLIBRARY_STANDARDS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if polklibrary.standards is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'polklibrary.standards'))

    def test_browserlayer(self):
        """Test that IPolklibraryStandardsLayer is registered."""
        from polklibrary.standards.interfaces import (
            IPolklibraryStandardsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPolklibraryStandardsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = POLKLIBRARY_STANDARDS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['polklibrary.standards'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if polklibrary.standards is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'polklibrary.standards'))

    def test_browserlayer_removed(self):
        """Test that IPolklibraryStandardsLayer is removed."""
        from polklibrary.standards.interfaces import \
            IPolklibraryStandardsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPolklibraryStandardsLayer,
            utils.registered_layers())
