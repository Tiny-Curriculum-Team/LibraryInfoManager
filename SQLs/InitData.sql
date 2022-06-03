-- Publisher Table Initialize
insert into Publisher(PublisherID, publisher_name) values ( 1, '商务印书馆' );
insert into Publisher(PublisherID, publisher_name) values ( 2, '人民出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 3, '人民文学出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 4, '作家出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 5, '译林出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 6, '中华书局' );
insert into Publisher(PublisherID, publisher_name) values ( 7, '社科文献出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 8, '生活-读书-新知三联书店' );
insert into Publisher(PublisherID, publisher_name) values ( 9, '中央编译出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 10, '国家图书馆出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 11, '科学出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 12, '清华大学出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 13, '机械工业出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 14, '电子工业出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 15, '化学工业出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 16, '建筑工业出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 17, '人民邮电出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 18, '中国水利水电出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 19, '中国电力出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 20, '北京科学技术出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 21, '中国金融出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 22, '中国财经出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 23, '中信出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 24, '中国经济出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 25, '法律出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 26, '中国法制出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 27, '中国政法大学出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 28, '人民法院出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 29, '清华大学出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 30, '中国人民大学出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 31, '北京大学出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 32, '高等教育出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 33, '人民教育出版社' );
insert into Publisher(PublisherID, publisher_name) values ( 34, '中国少年儿童新闻出版总社' );

-- Book Type Table Initialize
insert into BookType(BookTypeID, book_type_name) values ( 1, '马克思列宁主义、毛泽东思想、邓小平理论' );
insert into BookType(BookTypeID, book_type_name) values ( 2, '哲学、宗教' );
insert into BookType(BookTypeID, book_type_name) values ( 3, '社会科学总论' );
insert into BookType(BookTypeID, book_type_name) values ( 4, '政治、法律' );
insert into BookType(BookTypeID, book_type_name) values ( 5, '军事' );
insert into BookType(BookTypeID, book_type_name) values ( 6, '经济' );
insert into BookType(BookTypeID, book_type_name) values ( 7, '文化、科学、教育、体育' );
insert into BookType(BookTypeID, book_type_name) values ( 8, '语言、文字' );
insert into BookType(BookTypeID, book_type_name) values ( 9, '文学' );
insert into BookType(BookTypeID, book_type_name) values ( 10, '艺术' );
insert into BookType(BookTypeID, book_type_name) values ( 11, '历史、地理' );
insert into BookType(BookTypeID, book_type_name) values ( 12, '自然科学总论' );
insert into BookType(BookTypeID, book_type_name) values ( 13, '数理科学和化学' );
insert into BookType(BookTypeID, book_type_name) values ( 14, '天文学、地球科学' );
insert into BookType(BookTypeID, book_type_name) values ( 15, '生物科学' );
insert into BookType(BookTypeID, book_type_name) values ( 16, '医药、卫生' );
insert into BookType(BookTypeID, book_type_name) values ( 17, '农业科学' );
insert into BookType(BookTypeID, book_type_name) values ( 18, '工业技术' );
insert into BookType(BookTypeID, book_type_name) values ( 19, '交通运输' );
insert into BookType(BookTypeID, book_type_name) values ( 20, '航空、航天' );
insert into BookType(BookTypeID, book_type_name) values ( 21, '环境科学、安全科学' );
insert into BookType(BookTypeID, book_type_name) values ( 22, '综合性图书' );

-- Book Table Initialize;
insert into Book
    (ISBN, book_name, book_type_id, author, location, status, PublisherID)
    values
    ('989-28-79-70597-8', '你的第一本哲学书', '8', '托马斯.内格尔', '23-75-86', 'IN', 30),
    ('989-28-654-6930-3', '哲学家们都干了些什么', '20', '林欣浩', '56-99-58', 'IN', 4),
    ('989-28-79-52883-6', '大问题:简明哲学导论', '18', '罗伯特所罗门', '06-90-31', 'IN', 16),
    ('989-28-79-43574-5', '叔本华思想随笔', '16', '阿图尔叔本华', '35-09-71', 'IN', 25),
    ('989-28-654-5794-2', '人生的智慧', '10', '阿图尔叔本华', '91-04-36', 'IN', 33),
    ('989-28-79-44730-4', '悉达多', '21', '赫尔曼黑塞', '93-78-72', 'IN', 31),
    ('989-28-654-5771-3', '沉思录', '18', '马可奥勒留', '77-40-60', 'IN', 34),
    ('989-28-79-04510-4', '反脆弱', '9', '纳西姆-塔勒布', '75-42-94', 'IN', 17),
    ('989-28-79-18127-7', '箭术与禅心', '11', '奥根.赫立格尔', '91-52-59', 'IN', 13),
    ('989-28-79-68089-3', '社会契约论', '7', '卢梭', '08-89-51', 'IN', 31),
    ('989-28-79-22871-2', '活出生命的意义', '4', '维克多弗兰克', '95-69-31', 'IN', 32),
    ('989-28-79-01991-4', '活着', '18', '余华', '80-48-32', 'IN', 14),
    ('989-28-654-0047-4', '人间失格', '18', '太宰治', '78-87-32', 'IN', 24),
    ('989-28-79-67891-3', '平凡的世界', '10', '路遥', '03-10-00', 'IN', 33),
    ('989-28-654-2620-7', '人间草木', '17', '汪曾祺', '30-27-70', 'IN', 20),
    ('989-28-3705-054-6', '老人与海', '9', '欧内斯特海明威', '05-51-28', 'IN', 9),
    ('989-28-79-45675-7', '罪与罚', '5', '费奥多尔陀思妥耶夫斯基', '63-74-42', 'IN', 10),
    ('989-28-79-82749-6', '1Q84', '20', '村上春树', '20-37-90', 'IN', 1),
    ('989-28-79-30536-9', '三体', '10', '刘慈欣', '40-88-19', 'IN', 22),
    ('989-28-229-1404-4', '心理学与生活', '21', '理查德格里格/菲利普津巴多', '17-66-61', 'IN', 20),
    ('989-28-229-7592-2', '心流', '6', '米哈里契克森米哈赖', '02-18-36', 'IN', 27),
    ('989-28-3705-222-9', '乌合之众', '7', '勒庞', '54-15-75', 'IN', 9),
    ('989-28-79-69807-2', '人性的弱点全集', '14', '戴尔卡耐基', '20-64-03', 'IN', 1),
    ('989-28-79-42728-3', '社会性动物', '2', '埃利奥特阿伦森', '70-52-07', 'IN', 33),
    ('989-28-654-7965-4', '自控力', '20', '凯利麦格尼格尔', '83-13-09', 'IN', 11),
    ('989-28-79-87459-9', '被讨厌的勇气', '4', '岸见一郎/古贺史健', '87-44-60', 'IN', 6),
    ('989-28-229-6632-6', '亲密关系', '4', '罗兰米勒/丹尼尔.珀尔曼', '19-18-86', 'IN', 10),
    ('989-28-79-32105-5', '社会心理学', '17', '戴维迈尔斯', '68-88-72', 'IN', 7),
    ('989-28-79-71565-6', '营养圣经', '17', '帕特里克霍尔福德', '07-09-43', 'IN', 21),
    ('989-28-79-43841-8', '医生的精进', '2', '阿图葛文德', '75-59-15', 'IN', 34),
    ('989-28-79-61125-5', '医生的修炼', '15', '阿图葛文德', '76-75-11', 'IN', 5),
    ('989-28-654-0127-3', '营养圣经实用指南', '16', 'Patrick Holford/Susannah Lawson', '44-17-92', 'IN', 26),
    ('989-28-654-9826-6', '中国居民膳食指南', '4', '中国营养学会', '62-53-95', 'IN', 28),
    ('989-28-654-8573-0', '食物营养与配餐', '3', '范志红', '50-03-30', 'IN', 3),
    ('989-28-79-82125-8', '吃货的生物学修养', '5', '王立铭', '66-92-37', 'IN', 22),
    ('989-28-79-14379-4', '天生就会跑', '6', '克里斯托弗麦克杜格尔', '85-82-60', 'IN', 23),
    ('989-28-654-6033-1', '囚徒健身', '16', '保罗威德', '25-16-08', 'IN', 4),
    ('989-28-229-0197-6', '瑜伽之光', '4', 'B.K.S.艾扬格', '13-68-17', 'IN', 16),
    ('989-28-654-4370-9', '管理百年', '19', '斯图尔特克雷纳', '00-91-58', 'IN', 12),
    ('989-28-79-13801-1', '管理的实践', '7', '彼得德鲁克', '17-19-64', 'IN', 10),
    ('989-28-3705-633-3', '管理的常识', '5', '陈春花', '78-30-43', 'IN', 15),
    ('989-28-3705-987-7', '桌有成效的管理者', '16', '彼得德鲁克', '79-91-57', 'IN', 21),
    ('989-28-79-13871-4', '蓝海战略', '20', 'W钱金/勒妮-莫博涅', '97-43-36', 'IN', 32),
    ('989-28-79-05638-4', '认识商业', '6', '威廉尼科尔斯/詹姆斯麦克修/苏珊-麦克修', '92-51-32', 'IN', 27),
    ('989-28-79-91028-0', '麦肯锡问题分析与解决技巧', '18', '高杉尚孝', '47-95-60', 'IN', 5),
    ('989-28-3705-966-2', '科学的广告', '16', '克劳德霍普金斯', '80-44-14', 'IN', 29),
    ('989-28-3705-607-4', '影响力', '3', '罗伯特西奥迪尼', '06-21-75', 'IN', 6),
    ('989-28-229-5891-8', '富爸爸穷爸爸', '18', '罗伯特T清崎/莎伦.L.莱希特', '54-02-35', 'IN', 30),
    ('989-28-3705-592-3', '财富自由之路', '6', '李笑来', '88-12-65', 'IN', 9),
    ('989-28-79-82197-5', '股市真规则', '2', '帕特多尔西', '66-72-21', 'IN', 24),
    ('989-28-79-22562-9', '证券分析', '16', '本杰明格雷厄姆/戴维.多德', '88-56-32', 'IN', 18),
    ('989-28-79-40897-8', '彼得.林奇的成功投资', '2', '彼得林奇/约翰罗瑟查尔德', '15-87-04', 'IN', 18),
    ('989-28-79-23015-9', '小鸟经济学', '15', '彼得希夫/安德鲁.希夫', '53-41-35', 'IN', 30),
    ('989-28-3705-152-9', '手把手教你读财报', '20', '唐朝', '26-49-08', 'IN', 24),
    ('989-28-3705-583-1', '投资中最重要的事', '20', '霍华德马克斯', '58-85-48', 'IN', 6),
    ('989-28-79-07610-8', '穷查理宝典', '7', '彼得考夫曼', '10-56-24', 'IN', 6),
    ('989-28-3705-649-4', '巴菲特的护城河', '21', '帕特多尔西', '47-72-81', 'IN', 25),
    ('989-28-79-51397-9', '如何阅读一本书', '4', '莫提默艾德勒/查尔斯范多伦', '85-78-95', 'IN', 18),
    ('989-28-3705-775-0', '超级快速阅读', '12', '克里斯蒂安格吕宁', '00-88-28', 'IN', 1),
    ('989-28-79-05670-4', '学习之道', '8', '乔希维茨金', '52-62-67', 'IN', 8),
    ('989-28-3705-136-9', '奇特的一生', '1', '格拉宁', '30-88-67', 'IN', 16),
    ('989-28-79-56856-6', '怦然心动的人生整理魔法', '3', '近藤麻理惠', '29-43-73', 'IN', 33),
    ('989-28-79-26824-4', '谈谈方法》 ___', '19', '笛卡尔', '43-84-73', 'IN', 1),
    ('989-28-229-3157-7', '学会提问', '13', 'M尼尔布朗/斯图尔特基利', '89-24-51', 'IN', 29),
    ('989-28-3705-492-6', '刻意练习:如何从新手到大师', '22', '安德斯艾利克森/罗伯特.普尔', '69-58-74', 'IN', 31),
    ('989-28-3705-138-3', '金字塔原理', '8', '巴巴拉明托', '48-62-35', 'IN', 2),
    ('989-28-3705-007-2', '关键对话', '7', '科里帕特森/约瑟夫格雷尼/罗恩麦克米兰', '25-26-96', 'IN', 27),
    ('989-28-3705-369-1', '少有人走的路', '9', '斯科特派克', '75-70-26', 'IN', 15),
    ('989-28-79-23023-4', '搞定', '2', '戴维.艾伦', '62-56-16', 'IN', 3),
    ('989-28-79-21991-8', '改变', '1', '瓦茨拉维克/威克兰德/菲什', '97-06-37', 'IN', 27),
    ('989-28-79-68531-7', '深度工作', '1', '卡尔纽波特', '49-24-77', 'IN', 15),
    ('989-28-79-96705-5', '做出好决定', '4', '斯蒂芬P罗宾斯', '95-76-56', 'IN', 31),
    ('989-28-79-16826-1', '安静的力量', '8', '皮克耶尔', '56-66-78', 'IN', 1),
    ('989-28-654-2017-5', '远见', '18', '布赖恩费瑟斯通豪', '59-00-01', 'IN', 27),
    ('989-28-79-16533-8', '瞬变', '6', '奇普希思/丹希思', '69-20-40', 'IN', 4),
    ('989-28-79-69359-6', '原则', '18', '瑞达利欧', '16-79-39', 'IN', 4),
    ('989-28-79-16808-7', '认知：所谓成长就是认知升级', '5', '吴建平', '55-28-38', 'IN', 7),
    ('989-28-654-5018-9', '思考，快与慢', '4', '丹尼尔卡尼曼/Daniel Kahneman', '81-18-72', 'IN', 28),
    ('989-28-79-36485-4', '批判性思维教程', '8', '谷振诣', '21-44-87', 'IN', 5),
    ('989-28-79-27078-0', '非理性的人', '14', '威廉巴雷特', '51-84-88', 'IN', 28),
    ('989-28-79-55824-6', '占有还是存在', '9', '埃里希弗洛姆', '05-96-09', 'IN', 34),
    ('989-28-79-82339-9', '局外人', '3', '阿尔贝加缪', '42-80-54', 'IN', 1),
    ('989-28-654-9484-8', '堕落', '15', '阿尔贝加缪', '12-42-85', 'IN', 34),
    ('989-28-654-3988-7', '超越感觉（第九版）', '14', '文森特鲁吉罗', '30-56-69', 'IN', 26),
    ('989-28-79-86624-2', '娱乐至死', '16', '尼尔波兹曼', '29-28-58', 'IN', 1),
    ('989-28-79-64693-6', '暴力:六个侧面的反思', '18', '斯拉沃热齐泽克/Slavoi Zizek', '76-52-53', 'IN', 18),
    ('989-28-229-9769-6', '美丽新世界', '16', '阿道司赫胥黎', '63-97-97', 'IN', 9),
    ('989-28-3705-763-7', '理念的力量', '20', '张维迎', '76-18-37', 'IN', 33),
    ('989-28-79-74374-1', '爱的艺术', '8', '艾弗洛姆', '98-03-19', 'IN', 23),
    ('989-28-79-55752-2', '列奥纳多达芬奇传', '16', '沃尔特艾萨克森', '65-42-08', 'IN', 26),
    ('989-28-654-6507-7', '系统之美', '14', '德内拉梅多斯', '57-65-88', 'IN', 23),
    ('989-28-79-03683-6', '用心学泡茶', '11', '何厚余', '41-93-65', 'IN', 29),
    ('989-28-654-3899-6', '像艺术家一样思考', '11', '贝蒂艾德华', '12-05-90', 'IN', 14),
    ('989-28-79-11297-4', '设计中的设计', '16', '原研哉', '74-36-41', 'IN', 29),
    ('989-28-3705-205-2', '从地球到月球', '13', '儒勒凡尔纳', '62-42-76', 'IN', 34);

-- Reader Table Initialize
insert into Reader
    (ReaderID, reader_name, user_name, password, account_status, tel, trustworthiness, max_borrow_day, max_borrow_count)
    values
    ('10245045', '6aCwWHeqjS', 'ibJSH', 'e10adc3949ba59abbe56e057f20f883e', 'NORMAL', '13824737248', 100, 30, 10),
    ('10829841', 'YG46YGvkRz', 'Tsmp9', 'e10adc3949ba59abbe56e057f20f883e', 'NORMAL', '13389145778', 100, 30, 10),
    ('71109414', 'VPIGHfjJCm', 'PgLTC', 'e10adc3949ba59abbe56e057f20f883e', 'NORMAL', '13242615506', 100, 30, 10),
    ('24038364', 'RoJNR0a971', 'spS5X', 'e10adc3949ba59abbe56e057f20f883e', 'NORMAL', '13169776687', 100, 30, 10),
    ('25074716', '35aPFh7PO2', 'jfXR7', 'e10adc3949ba59abbe56e057f20f883e', 'NORMAL', '13221123254', 100, 30, 10);

-- Admin Table Initialize
insert into Administrator
    (WorkID, admin_name, user_name, password, tel)
    values
    (0, 'Root', 'root', '4399', '12908573549');
