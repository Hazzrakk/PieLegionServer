from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_11/models/lawbotHQ/LB_Zone04a',
        'wantDoors': 1},
 0: {'type': 'zone',
     'name': 'UberZone',
     'comment': '',
     'parentEntId': 0,
     'scale': 1,
     'description': '',
     'visibility': []},
 100018: {'type': 'button',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(54.7666, 7.03896, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(3, 3, 3),
          'color': Vec4(1, 1, 1, 1),
          'isOn': 0,
          'isOnEvent': 0,
          'secondsOn': -1.0},
 100019: {'type': 'button',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-58.0835, 7.37219, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(3, 3, 3),
          'color': Vec4(1, 1, 1, 1),
          'isOn': 0,
          'isOnEvent': 0,
          'secondsOn': -1.0},
 100015: {'type': 'door',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 100005,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'color': Vec4(1, 1, 1, 1),
          'isLock0Unlocked': 0,
          'isLock1Unlocked': 1,
          'isLock2Unlocked': 0,
          'isLock3Unlocked': 1,
          'isOpen': 0,
          'isOpenEvent': 0,
          'isVisBlocker': 1,
          'secondsOpen': 1,
          'unlock0Event': 100016,
          'unlock1Event': 0,
          'unlock2Event': 100017,
          'unlock3Event': 0},
 100016: {'type': 'laserField',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-15.1345, -13.2285, 0.25),
          'hpr': Point3(90, 0, 0),
          'scale': Vec3(1, 1, 1),
          'cellId': 0,
          'gridGame': 'Random',
          'gridScaleX': 42.0,
          'gridScaleY': 40.0,
          'laserFactor': 3,
          'modelPath': 0,
          'projector': Point3(20, 40, 45),
          'switchId': 100019},
 100017: {'type': 'laserField',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(11.2941, 28.7739, 0.28),
          'hpr': Vec3(270, 0, 0),
          'scale': Vec3(1, 1, 1),
          'cellId': 1,
          'gridGame': 'Random',
          'gridScaleX': 42.0,
          'gridScaleY': 40.0,
          'laserFactor': 3,
          'modelPath': 0,
          'projector': Point3(20, 40, 45),
          'switchId': 100018},
 100001: {'type': 'model',
          'name': 'copy of partition (3)',
          'comment': '',
          'parentEntId': 100000,
          'pos': Point3(-8.98508, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100002: {'type': 'model',
          'name': 'copy of partition (4)',
          'comment': '',
          'parentEntId': 100000,
          'pos': Point3(5.36486, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100003: {'type': 'model',
          'name': 'copy of partition (5)',
          'comment': '',
          'parentEntId': 100000,
          'pos': Point3(20.1513, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100004: {'type': 'model',
          'name': 'copy of partition (6)',
          'comment': '',
          'parentEntId': 100000,
          'pos': Point3(34.9439, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100007: {'type': 'model',
          'name': 'copy of partition',
          'comment': '',
          'parentEntId': 100006,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100008: {'type': 'model',
          'name': 'copy of partition (2)',
          'comment': '',
          'parentEntId': 100006,
          'pos': Point3(-14.9029, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Point3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100009: {'type': 'model',
          'name': 'copy of partition (3)',
          'comment': '',
          'parentEntId': 100006,
          'pos': Point3(-29.7119, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100010: {'type': 'model',
          'name': 'copy of partition (4)',
          'comment': '',
          'parentEntId': 100006,
          'pos': Point3(-44.4821, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100012: {'type': 'model',
          'name': 'copy of partition (3)',
          'comment': '',
          'parentEntId': 100011,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100013: {'type': 'model',
          'name': 'copy of partition (4)',
          'comment': '',
          'parentEntId': 100011,
          'pos': Point3(-14.9149, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100014: {'type': 'model',
          'name': 'copy of partition (5)',
          'comment': '',
          'parentEntId': 100011,
          'pos': Point3(-29.7289, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100023: {'type': 'model',
          'name': 'copy of partition (6)',
          'comment': '',
          'parentEntId': 100011,
          'pos': Point3(-44.4361, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100025: {'type': 'model',
          'name': 'copy of partition (7)',
          'comment': '',
          'parentEntId': 100000,
          'pos': Point3(42.3323, -38.4749, 0),
          'hpr': Vec3(270, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100026: {'type': 'model',
          'name': 'copy of partition (8)',
          'comment': '',
          'parentEntId': 100000,
          'pos': Point3(42.3323, -25.7861, 0),
          'hpr': Vec3(270, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100027: {'type': 'model',
          'name': 'copy of partition (5)',
          'comment': '',
          'parentEntId': 100006,
          'pos': Point3(-52.4944, -39.8953, 0),
          'hpr': Vec3(270.818, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100028: {'type': 'model',
          'name': 'copy of partition (6)',
          'comment': '',
          'parentEntId': 100006,
          'pos': Point3(-52.4944, -25.343, 0),
          'hpr': Vec3(270.818, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100029: {'type': 'model',
          'name': 'scenary',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-38.0023, -20.533, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_couchA.bam'},
 100030: {'type': 'model',
          'name': 'copy of scenary',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-28.9763, -28.2505, 0),
          'hpr': Vec3(270, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_couchA.bam'},
 100031: {'type': 'model',
          'name': 'copy of scenary (2)',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-51.8392, -28.2505, 0),
          'hpr': Vec3(131.894, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_bookshelfB.bam'},
 100032: {'type': 'model',
          'name': 'copy of scenary (3)',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-44.1843, -37.0309, 0),
          'hpr': Vec3(131.894, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_bookshelfB.bam'},
 100033: {'type': 'model',
          'name': 'copy of scenary (4)',
          'comment': '',
          'parentEntId': 100034,
          'pos': Point3(16.5447, -16.1896, 0),
          'hpr': Vec3(358.668, 0, 0),
          'scale': Point3(2, 2, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam'},
 100037: {'type': 'model',
          'name': 'partition',
          'comment': '',
          'parentEntId': 100036,
          'pos': Point3(-14.6846, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100038: {'type': 'model',
          'name': 'copy of partition',
          'comment': '',
          'parentEntId': 100036,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100039: {'type': 'model',
          'name': 'copy of partition',
          'comment': '',
          'parentEntId': 100036,
          'pos': Point3(15.087, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100040: {'type': 'model',
          'name': 'copy of partition (2)',
          'comment': '',
          'parentEntId': 100036,
          'pos': Point3(-29.9877, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100041: {'type': 'model',
          'name': 'copy of scenary (5)',
          'comment': '',
          'parentEntId': 100034,
          'pos': Point3(20.0815, -16.1896, 0),
          'hpr': Vec3(358.668, 0, 0),
          'scale': Point3(2, 2, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam'},
 100042: {'type': 'model',
          'name': 'copy of scenary (6)',
          'comment': '',
          'parentEntId': 100034,
          'pos': Point3(31.1973, -15.8974, 0),
          'hpr': Vec3(358.668, 0, 0),
          'scale': Point3(1, 1, 1),
          'collisionsOnly': 0,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/LB_bookshelfA.bam'},
 100043: {'type': 'model',
          'name': 'box',
          'comment': '',
          'parentEntId': 100000,
          'pos': Point3(-10.7296, -3.52948, 0),
          'hpr': Vec3(270.924, 0, 0),
          'scale': Point3(2, 8, 2),
          'collisionsOnly': 1,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100044: {'type': 'model',
          'name': 'copy of box',
          'comment': '',
          'parentEntId': 100036,
          'pos': Point3(-32.0389, 7.09736, 0),
          'hpr': Vec3(90, 0, 0),
          'scale': Point3(1, 8, 2),
          'collisionsOnly': 1,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100045: {'type': 'model',
          'name': 'copy of box (2)',
          'comment': '',
          'parentEntId': 100006,
          'pos': Point3(2.05698, -7.92436, 0),
          'hpr': Vec3(270, 0, 0),
          'scale': Point3(2, 8, 2),
          'collisionsOnly': 1,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 100046: {'type': 'model',
          'name': 'copy of box (3)',
          'comment': '',
          'parentEntId': 100011,
          'pos': Point3(1.66589, 6.97288, 0),
          'hpr': Vec3(270, 0, 0),
          'scale': Point3(2, 8, 2),
          'collisionsOnly': 1,
          'flattenType': 'light',
          'loadType': 'loadModelCopy',
          'modelPath': 'phase_11/models/lawbotHQ/PartitionA.bam'},
 10000: {'type': 'nodepath',
         'name': '0',
         'comment': '',
         'parentEntId': 100035,
         'pos': Point3(-64.0541, 7.6285, 0),
         'hpr': Vec3(90, 0, 0),
         'scale': Point3(1, 1, 1)},
 100020: {'type': 'nodepath',
          'name': 'battle place 1',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-35.0928, 6.21518, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100021: {'type': 'nodepath',
          'name': 'cogparent2',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(64.2291, 5.46719, 0),
          'hpr': Vec3(270, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100022: {'type': 'nodepath',
          'name': 'BattlePlace2',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(32.4809, 7.68949, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100035: {'type': 'nodepath',
          'name': 'cogparent1',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100000: {'type': 'rendering',
          'name': 'PartitionWall2',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-53.71, -14.4718, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'blending': 'Alpha',
          'colorA': 1.0,
          'colorB': 1.0,
          'colorG': 1.0,
          'colorR': 1.0,
          'fogOn': 0,
          'renderBin': 'transparent'},
 100005: {'type': 'rendering',
          'name': 'doorparent',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-0.845594, 73.9927, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'blending': 'Normal',
          'colorA': 1.0,
          'colorB': 0.75,
          'colorG': 0.75,
          'colorR': 0.8,
          'fogOn': 0,
          'renderBin': 'transparent'},
 100006: {'type': 'rendering',
          'name': 'wallparent3',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(61.7299, -14.6471, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'blending': 'Alpha',
          'colorA': 1.0,
          'colorB': 1.0,
          'colorG': 1.0,
          'colorR': 1.0,
          'fogOn': 0,
          'renderBin': 'transparent'},
 100011: {'type': 'rendering',
          'name': 'wallprent4',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(62.3555, 30.4101, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'blending': 'Alpha',
          'colorA': 1.0,
          'colorB': 1.0,
          'colorG': 1.0,
          'colorR': 1.0,
          'fogOn': 0,
          'renderBin': 'transparent'},
 100024: {'type': 'rendering',
          'name': 'cogrenderingparent2',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(64.2291, 5.46719, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'blending': 'Additive',
          'colorA': 1.0,
          'colorB': 0.0,
          'colorG': 0.0,
          'colorR': 1.0,
          'fogOn': 0,
          'renderBin': 'fixed'},
 100034: {'type': 'rendering',
          'name': 'scenaryLight',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': 1,
          'blending': 'Alpha',
          'colorA': 1.0,
          'colorB': 0.5,
          'colorG': 0.5,
          'colorR': 0.6,
          'fogOn': 0,
          'renderBin': 'transparent'},
 100036: {'type': 'rendering',
          'name': 'partitionwall1',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-33.8745, 29.3783, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'blending': 'Normal',
          'colorA': 1.0,
          'colorB': 1.0,
          'colorG': 1.0,
          'colorR': 1.0,
          'fogOn': 0,
          'renderBin': 'transparent'}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}
