def converter_atom_para_rss(caminho_arquivo_atom, caminho_arquivo_rss):
    # Analisa o arquivo .atom
    arvore = ET.parse(caminho_arquivo_atom)
    raiz = arvore.getroot()

    # Cria um elemento raiz para .RSS
    rss = ET.Element('rss', version='2.0')
    canal = ET.SubElement(rss, 'channel')

    # Mapeia elementos .atom para elementos .RSS
    for elem in raiz:
        if elem.tag.endswith('title'):
            titulo = ET.SubElement(canal, 'title')
            titulo.text = elem.text
        elif elem.tag.endswith('link'):
            link = ET.SubElement(canal, 'link')
            link.text = elem.attrib.get('href', '')
        elif elem.tag.endswith('updated'):
            dataUltimaConstrucao = ET.SubElement(canal, 'lastBuildDate')
            dataUltimaConstrucao.text = elem.text
        elif elem.tag.endswith('entry'):
            item = ET.SubElement(canal, 'item')
            for elem_entrada in elem:
                if elem_entrada.tag.endswith('title'):
                    titulo_item = ET.SubElement(item, 'title')
                    titulo_item.text = elem_entrada.text
                elif elem_entrada.tag.endswith('link'):
                    link_item = ET.SubElement(item, 'link')
                    link_item.text = elem_entrada.attrib.get('href', '')
                elif elem_entrada.tag.endswith('summary'):
                    descricao = ET.SubElement(item, 'description')
                    descricao.text = elem_entrada.text

    # Cria uma nova árvore XML para RSS
    arvore_rss = ET.ElementTree(rss)

    # Escreve a árvore RSS em um arquivo
    arvore_rss.write(caminho_arquivo_rss, encoding='utf-8', xml_declaration=True)