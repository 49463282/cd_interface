from selenium import webdriver
from time import sleep

from selenium.common.exceptions import NoSuchElementException

list = [
    'Abdominal Manual Therapy Repairs Interstitial Cells of Cajal and Increases Colonic c-Kit Expression When Treating Bowel Dysfunction after Spinal Cord Injury',
    'Effects of Electroacupuncture on the Daily Rhythmicity of Intestinal Movement and CircadianRhythmicity of Colonic Per2 Expression in Rats with Spinal Cord Injury',
    'Electroacupuncture at Zusanli (ST36) ameliorates colonic neuronal nitric oxide synthaseupregulation in rats with neurogenic bowel dysfunction following spinal cord injury',
    'Effectiveness and safety of Chinese massage therapy (Tui Na) on post-stroke spasticity: a prospective multicenter randomized controlled trial',
    'Surgical versus non-surgical treatment for vertebral compression fracture with osteopenia: a systematic review and meta-analysis',
    'Tai Chi for improving cardiopulmonary function and quality of life in patients with chronic obstructive pulmonary disease: A systematic review and meta-analysis',
    ' Clinical Rehabilitation',
    'Efficiency of muscle strength training on motor function in patients with coronary artery disease: a meta-analysis',
    'Sling Exercise for Chronic Low Back Pain: A Systematic Review and Meta-Analysis',
    'Research progress on the central mechanism underlying regulation of visceral biological rhythm by per2 (Review)',
    '加速康复外科从recovery到rehabilitation']
for i in list:
    driver = webdriver.Chrome()
    driver.get('https://xueshu.baidu.com/')
    driver.find_element_by_id('kw').send_keys(i)
    driver.find_element_by_id('su').click()
    try:
        name = driver.find_element_by_class_name('author_text').text
        title = driver.find_element_by_class_name('container_right').text
        time = driver.find_element_by_class_name('doi_wr').text
        unit = len(name.split("，"))
    except:
        time = 'null'
        name = 'null'
        title = 'null'
        unit = 'null'  # 抛出异常，注释后则不抛出异常
    print(i)
    print(time[-12:-5])
    print(time)
    print(name)
    print(title)
    print(unit)
    sleep(3)
    driver.quit()
