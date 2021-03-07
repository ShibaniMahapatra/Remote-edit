from setuptools import setup, find_packages

# -*- coding: utf-8 -*-
"""flaskcode module setup"""

setup(
    name='title',
    version='1.0.0',
    license='MIT',
    author='Shibani Mahapatra',
    author_email='shibani.mahapatra47@gmail.com',
    url='',
    description='',
    long_description='',
    long_description_content_type='text/markdown',
    keywords='flaskcode code editor code-editor',
    packages=['flaskcode'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    entry_points={
        'console_scripts': [
            'remote_edit = remote_edit.cli:main',
        ]
    },
    python_requires='>=2.7.0',
    install_requires=[
        'pyngrok>=4.1.12',
        'flaskcode',
        'subprocess.run>=0.0.8'
    ],

    classifiers=[
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Text Editors :: Text Processing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)