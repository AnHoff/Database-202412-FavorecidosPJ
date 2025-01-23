CREATE DATABASE IF NOT EXISTS 202412_FavorecidosPJ;
USE 202412_FavorecidosPJ;

CREATE TABLE IF NOT EXISTS CNAE (
    COD_SECAO CHAR(1) NOT NULL,              			-- Código da seção (letra única)
    DESC_SECAO VARCHAR(255) NOT NULL,        		
    COD_SUBCLASSE INT(9) NOT NULL,              		-- Código da subclasse
    DESC_SUBCLASSE VARCHAR(255) NOT NULL,     		
    PRIMARY KEY (COD_SUBCLASSE)
);

CREATE TABLE IF NOT EXISTS NaturezaJuridica (
    COD_NATJURIDICA INT(4) NOT NULL,               		-- Código da natureza jurídica
    DESC_NATJURIDICA VARCHAR(255) NOT NULL,    		
    COD_TIPO_NATJURIDICA INT(9) NOT NULL,         		-- Código do tipo de natureza jurídica
    DESC_TIPO_NATJURIDICA VARCHAR(255) NOT NULL, 	
	PRIMARY KEY (COD_NATJURIDICA)
);

CREATE TABLE IF NOT EXISTS CNPJ (
    CNPJ bigint NOT NULL,                          
    RAZAOSOCIAL VARCHAR(255) NOT NULL,          
    NOMEFANTASIA VARCHAR(255),                  
    COD_CNAE INT(9),                           -- Código CNAE
    COD_NATJURIDICA INT(4),                    -- Código da natureza jurídica
    TIPO_PESSOA VARCHAR(255),                   
    LOGRADOURO VARCHAR(255),                    
    NUMERO VARCHAR(50),                         		-- Número (aceita 'SN' ou outros textos)
    COMPLEMENTO VARCHAR(255),                   
    CEP VARCHAR(20),                            
    BAIRRO VARCHAR(255),                        
    MUNICIPIO VARCHAR(255),                     
    UF CHAR(2),
    PRIMARY KEY (CNPJ),
    FOREIGN KEY (COD_NATJURIDICA)               
        REFERENCES NaturezaJuridica(COD_NATJURIDICA)
        ON DELETE SET NULL         
        ON UPDATE CASCADE,
	FOREIGN KEY (COD_CNAE)
		REFERENCES CNAE(COD_SUBCLASSE)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

