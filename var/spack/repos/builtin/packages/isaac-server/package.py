# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class IsaacServer(CMakePackage):
    """In Situ Animation of Accelerated Computations: Server"""

    homepage = "http://computationalradiationphysics.github.io/isaac/"
    url      = "https://github.com/ComputationalRadiationPhysics/isaac/archive/v1.3.0.tar.gz"
    git      = "https://github.com/ComputationalRadiationPhysics/isaac.git"

    maintainers = ['ax3l']

    version('develop', branch='dev')
    version('master', branch='master')
    version('1.4.0', sha256='6cbd4cc54a22de5e5a3427e44141db6e7b80b33fe7a0c707390a113655bf344e')
    version('1.3.3', sha256='92a972d05d315ad66546671c047b7edf8ed0e05d64d2b8d77ababb5bb9b93d8e')
    version('1.3.2', sha256='e6eedc641de5b0a7c5ea5cda6b11e9b6d4a78dfac8be90302147b26d09859a68')
    version('1.3.1', sha256='7dead8f3d5467cbd2cde8187e7b860a4ab7796348895d18291f97a76e28757cf')
    version('1.3.0', sha256='fcf10f4738e7790ef6604e1e2cdd052a129ba4e53a439deaafa9fb2a70585574')

    # variant('gstreamer', default=False, description= \
    #         'Support for RTP streams, e.g. to Twitch or Youtube')

    depends_on('cmake@3.3:', type='build')
    depends_on('jpeg', type='link')
    depends_on('jansson', type='link')
    depends_on('boost@1.56.0:', type='link')
    depends_on('libwebsockets@2.1.1:', type='link')
    # depends_on('gstreamer@1.0', when='+gstreamer')

    # https://github.com/ComputationalRadiationPhysics/isaac/pull/70
    patch('jpeg.patch', when='@:1.3.1')
    patch('arm.patch', when='@:1.4.0 target=aarch64:')

    root_cmakelists_dir = 'server'
