# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

from frappe.model.document import Document

class WebsiteSlideshow(Document):
		
	def on_update(self):
		# a slide show can be in use and any change in it should get reflected
		from frappe.website.render import clear_cache
		clear_cache()
		
def get_slideshow(bean):
	slideshow = frappe.bean("Website Slideshow", bean.doc.slideshow)
	
	return {
		"slides": slideshow.doclist.get({"doctype":"Website Slideshow Item"}),
		"slideshow_header": slideshow.doc.header or ""
	}
