# This script is written in Python (Jython implementation 2.5.3)
# See the Help menu for tutorials, example scripts and API
#   m_Mango_mango (class m_Mango) represents the application
# Select a class in the API guide below to view its properties and methods
m_VolMan_result = m_Mango_mango.makeNewVolumeManager(
    *getMultiInput(
        None,
        "makeNewVolumeManager",
        ["openLocation"],
        ["string"],
        ["/Users/dschonhaut/data/IDEAS_FullAnalysis/all_niftis/w50071.nii"],
    )
)
m_Mango_mango.setCurrentVolumeManager(m_VolMan_result)
m_Mango_mango.setWorldMode(True)
m_VolMan_result.setRoiColor(0)
m_VolMan_result.loadROI(
    *getMultiInput(
        None,
        "loadROI",
        ["openLocation"],
        ["string"],
        ["/Users/dschonhaut/data/IDEAS_FullAnalysis/ROIs_rPOP/ctx_voi_bin.nii"],
    )
)
m_VolMan_result.setCurrentSeriesPoint(0)
m_VolMan_result.setRoiColor(3)
m_VolMan_result.loadROI(
    *getMultiInput(
        None,
        "loadROI",
        ["openLocation"],
        ["string"],
        ["/Users/dschonhaut/data/IDEAS_FullAnalysis/ROIs_rPOP/wc_voi_bin.nii"],
    )
)
m_VolMan_result.setCurrentSeriesPoint(0)
