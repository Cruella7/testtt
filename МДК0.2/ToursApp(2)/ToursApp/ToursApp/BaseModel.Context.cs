﻿//------------------------------------------------------------------------------
// <auto-generated>
//     Этот код создан по шаблону.
//
//     Изменения, вносимые в этот файл вручную, могут привести к непредвиденной работе приложения.
//     Изменения, вносимые в этот файл вручную, будут перезаписаны при повторном создании кода.
// </auto-generated>
//------------------------------------------------------------------------------

namespace ToursApp
{
    using System;
    using System.Data.Entity;
    using System.Data.Entity.Infrastructure;
    
    public partial class TourBaseEntities : DbContext
    {
        private static TourBaseEntities _context;
        public TourBaseEntities()
            : base("name=TourBaseEntities")
        {
        }

        public static TourBaseEntities GetContext()
        {
            if (_context == null)
                _context = new TourBaseEntities();

            return _context;
        }
        

        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            throw new UnintentionalCodeFirstException();
        }
    
        public virtual DbSet<Country> Countries { get; set; }
        public virtual DbSet<Hotel> Hotels { get; set; }
        public virtual DbSet<HotelComment> HotelComments { get; set; }
        public virtual DbSet<Hotelimage> Hotelimages { get; set; }
        public virtual DbSet<sysdiagram> sysdiagrams { get; set; }
        public virtual DbSet<Tour> Tours { get; set; }
        public virtual DbSet<Type> Types { get; set; }
    }
}
