def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('io', parent_package, top_path)

    config.add_extension('_test_fortran',
                         sources=['_test_fortran.pyf', '_test_fortran.f'])

    config.add_data_dir('tests')
    config.add_subpackage('matlab')
    config.add_subpackage('arff')
    config.add_subpackage('_harwell_boeing')
    config.add_subpackage('_fast_matrix_market')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
