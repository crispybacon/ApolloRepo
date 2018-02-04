import os, random, shutil
custom_image_directory = '/usr/share/backgrounds/'
def open_xml_file(file_name):
    file_start = '''<background>
    <starttime>
        <year>2010</year>
        <month>03</month>
        <day>01</day>
        <hour>07</hour>
        <minute>00</minute>
        <second>00</second>
    </starttime>
    '''
    with open(file_name, 'w') as f:
        f.write(file_start)
def randomize_image_list(image_dir):
    image_list = os.listdir(image_dir)
    image_list = [image for image in image_list if not image.startswith('.') and not image.endswith('xml')]
    random.shuffle(image_list)
    return image_list
    
def write_transitions(duration, image_path, image_list, xml_file):
    if not image_path.endswith('/'):
        image_path = image_path + '/'
    first_wallpaper = '''
    <static>
        <duration>{}</duration>
        <file>{}</file>
    </static>
    '''.format(duration, image_path + image_list[0])
    last_image = image_path + image_list[0]
    with open(xml_file, 'a') as f:
        f.write(first_wallpaper)
        for img in image_list[1:]:
            img = image_path + img
            transition = '''
    <transition type="fade">
        <duration>3.0</duration>
        <from>{}</from>
        <to>{}</to>
    </transition>
    <static>
        <duration>{}</duration>
        <file>{}</file>
    </static>
'''.format(last_image, img, duration, img)
            f.write(transition)
            last_image = img
        end = '</background>'
        f.write(end)
    return 'Wrote transitions to {}'.format(xml_file) 
def update_backgrounds(image_path, xml_file, duration):
    image_list = randomize_image_list(image_path)
    open_xml_file(xml_file)
    write_transitions(duration, image_path, image_list, xml_file)
def copyXML(xml_file, custom_kiosk_directory):
    if not os.path.exists(custom_image_directory):
        os.mkdir(custom_kiosk_directory)
    shutil.copy(xml_file, custom_image_directory)

if __name__ == '__main__':
    update_backgrounds(custom_image_directory, 'default.xml', 300)
    copyXML('default.xml', custom_image_directory)
