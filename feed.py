import yaml;
import xml.etree.ElementTree as elTree;

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    rss_element = elTree.Element('rss', {
        'version':'2.0',
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/'
    });

channel_element = elTree.SubElement(rss_element, 'channel');

link_prefix = yaml_data['link'];

# Header Data
elTree.SubElement(channel_element, 'title').text = yaml_data['title'];
elTree.SubElement(channel_element, 'format').text = yaml_data['format'];
elTree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle'];
elTree.SubElement(channel_element, 'itunes:author').text = yaml_data['author'];
elTree.SubElement(channel_element, 'description').text = yaml_data['title'];
elTree.SubElement(channel_element, 'itunes:image', { 'href': link_prefix + yaml_data['image']});
elTree.SubElement(channel_element, 'link').text = link_prefix
elTree.SubElement(channel_element, 'language').text = yaml_data['language'];
elTree.SubElement(channel_element, 'itunes:category', { 'text': yaml_data['category']});

# Item Data
for item in yaml_data['item']:
    item_element = elTree.SubElement(channel_element, 'item')
    elTree.SubElement(item_element, 'title').text = item['title']
    elTree.SubElement(item_element, 'itunes:author').text = yaml_data['author']
    elTree.SubElement(item_element, 'description').text = item['description']
    elTree.SubElement(item_element, 'itunes:duration').text = item['duration']
    elTree.SubElement(item_element, 'pubDate').text = item['published']

    enclosure = elTree.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['file'],
        'type': 'audio/mpeg',
        'length': item['length']
    });

output_tree = elTree.ElementTree(rss_element);
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True);