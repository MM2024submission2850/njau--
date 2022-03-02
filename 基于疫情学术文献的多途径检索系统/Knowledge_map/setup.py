from setuptools import setup

# 列出软件包的相关依赖，可以通过'pip install -e’查看
requires = ['django==2.2',
            'beautifulsoup4==4.9.1',
            'requests',
            ]

# 开发人员需要的依赖，`pip install -e ".[dev]"`查看
dev_requires = ['pytest',
                'webtest',
                'django-livereload-server',  # 使用python manage.py livereload启动
                'django-debug-toolbar',
                'django-cors-headers',      # cors同源策略管理
                ]

setup(
    name='Knowledge_map',
    install_requires=requires,
    extras_require={'dev': dev_requires},
    entry_points={
        'paste.app_factory': [
            'main=Knowledge_map:main'
        ]
    },
)
