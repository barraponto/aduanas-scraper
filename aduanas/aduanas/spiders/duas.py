# -*- coding: utf-8 -*-
import scrapy
from aduanas.items import AduanasItemLoader


class DuasSpider(scrapy.Spider):
    name = "duas"
    allowed_domains = ["servicios.aduanas.gub.uy"]

    def parse(self, response):
        loader = AduanasItemLoader(response=response)
        loader.add_css('fecha', '#span_FECH_INGSI::text')
        loader.add_css('hora', '#span_HORA_INGSI::text')
        loader.add_css('tipo_aforo', '#span_TIPO_AFORO::text')
        loader.add_css('canal_aforo', '#span_vVTAFORDSC::text')
        loader.add_css('importador_tipo_documento', '#span_vCTIPODOC::text')
        loader.add_css('importador_documento', '#span_vCDOCUMEN::text')
        loader.add_css('importador_nombre', '#span_vDNOMBRE2::text')
        loader.add_css('facturas_codigo_moneda', '#span_CODI_MONED::text')
        loader.add_css('facturas_moneda', '#span_vVMONDSC::text')
        loader.add_css('facturas_total', '#span_TOT_FACT::text')
        loader.add_css('cif_total', '#span_TCIF_DOLPO::text')
        loader.add_css('aduanas_total', '#span_TVAD_INCR::text')
        loader.add_css('peso_bruto', '#span_TPESO_BRUT::text')
        loader.add_css('peso_neto', '#span_TPESO_NETO::text')
        loader.add_css('transporte', '#span_VIA_TRANSP::text')
        loader.add_css('aduana_codigo', '#span_vVADUIS::text')
        loader.add_css('aduana_nombre', '#span_vVADUDSC2::text')
        loader.add_css('tributos', '#span_TOTP_MN::text')
        return loader.load_item()
