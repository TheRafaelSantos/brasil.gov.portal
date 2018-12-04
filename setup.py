# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '2.1'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(
    name='brasil.gov.portal',
    version=version,
    description="Implementação Modelo da Identidade Digital de Governo",
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Multimedia",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='plone .gov.br identidade_digital egov',
    author='PloneGov.BR',
    author_email='gov@plone.org.br',
    url='https://github.com/plonegovbr/brasil.gov.portal',
    license='GPLv2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['brasil', 'brasil.gov'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'AccessControl',
        'Acquisition',
        'brasil.gov.agenda',
        'brasil.gov.barra',
        'brasil.gov.portlets',
        'brasil.gov.temas',
        'brasil.gov.tiles',
        'brasil.gov.vcge [dexterity]',
        'collective.cover',
        'collective.fingerpointing',
        'collective.jsonmigrator',
        'collective.lazysizes',
        'collective.liveblog',
        'collective.nitf',
        'collective.polls',
        'collective.upload',
        'five.pt',
        'lxml',
        'plone.api',
        'plone.app.content',
        'plone.app.contenttypes',
        'plone.app.controlpanel',
        'plone.app.dexterity',
        'plone.app.layout',
        'plone.app.registry',
        'plone.app.search',
        'plone.app.theming',
        'plone.app.viewletmanager',
        'plone.autoform',
        'plone.batching',
        'plone.contentrules',
        'plone.dexterity',
        'plone.formwidget.namedfile',
        'plone.i18n',
        'plone.indexer',
        'plone.memoize',
        'plone.namedfile',
        'plone.portlets',
        'plone.protect >= 3.0.26',
        'plone.registry',
        'plone.restapi',
        'plone.supermodel',
        'plone4.csrffixes',
        'Products.CMFCore',
        'Products.CMFDefault',
        'Products.CMFPlone',
        'Products.Doormat',  # TODO: remove in IDG 3.0
        'Products.GenericSetup',
        'Products.PloneFormGen',
        'Products.PloneKeywordManager',
        'Products.RedirectionTool',
        'Products.TinyMCE',
        'sc.contentrules.groupbydate',
        'sc.contentrules.layout',
        'sc.contentrules.metadata',
        'sc.embedder',
        'sc.photogallery',
        'sc.social.like',
        'setuptools',
        'six',
        'webcouturier.dropdownmenu',
        'z3c.form',
        'z3c.jbot',
        'z3c.unconfigure',
        'zope.component',
        'zope.formlib',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.schema',
        'Zope2',
    ],
    extras_require={
        'migration': [
            'collective.jsonmigrator',
            'collective.transmogrifier',
            'plone.app.transmogrifier',
            'transmogrify.dexterity',
        ],
        'test': [
            'plone.app.robotframework[debug]',
            'plone.app.testing [robot]',
            'plone.browserlayer',
            'plone.folder',
            'plone.testing',
            'plonetheme.sunburst',
            'Products.GenericSetup',
            'robotframework-wavelibrary',
            'robotsuite',
            'transaction',
            'zope.publisher',
            'zope.viewlet',
        ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
